'''star.py'''

import re
import logging
from ..models import StarTable, OrbitTable

LOGGER = logging.getLogger(__name__)
# LOGGER.setLevel(logging.DEBUG)


class Star(object):
    '''Star class'''
    def __init__(self, code):
        self.type = None
        self.decimal = None
        self.size = None
        self.min_orbit = 0
        self.hz_orbit = None
        self.int_orbit = None
        self.magnitude = 0
        self.luminosity = 0
        self.temperature = 0
        self.radius = 0
        self.mass = 0
        self.hz_period = None
        self.classification = None
        self._validate_code(code)
        self.get_classification()
        self.get_details()
        self.calculate_hz_period()

    def _validate_code(self, code):
        '''Validate code -> type, decimal, size'''
        LOGGER.debug('code = %s', code)
        if code:
            if code.endswith('D'):
                self._validate_code_dwarf(code)
            else:
                self._validate_code_star(code)

    def _validate_code_star(self, code):
        '''Validate code for non-dwarf'''
        mtch = re.match(
            r'([OBAFGKM])([0-9])\s*([IVDab]{1,2}$)',
            code)
        if mtch:
            LOGGER.debug('Code matches RE')
            self.type = mtch.group(1)
            self.decimal = int(mtch.group(2))
            if mtch.group(3) in ['Ia', 'Ib', 'II', 'III', 'IV', 'V', 'VI']:
                self.size = mtch.group(3)
            else:
                raise TypeError
            LOGGER.debug(
                'type = %s decimal = %s size = %s',
                self.type, self.decimal, self.size)

            # Check for invalid types
            if self.size == 'IV':
                LOGGER.debug('size = IV')
                # M[0-9] IV not possible, use V instead
                if self.type == 'M':
                    LOGGER.debug('type = M, setting size=V')
                    self.size = 'V'
                # K[5-9] IV not possible, use V instead
                if self.type == 'K' and self.decimal >= 5:
                    LOGGER.debug('type = K, size = 5-9, setting size=V')
                    self.size = 'V'
            if self.size == 'VI':
                # B[0-9] VI not possible, use V instead
                if self.type == 'B':
                    self.size = 'V'
                # F[0-4] VI not possible, use V instead
                if self.type == 'F' and self.decimal <= 4:
                    self.size = 'V'

    def _validate_code_dwarf(self, code):
        '''Validate code for dwarf'''
        mtch = re.match(r'([OBAFGKM])\s*D', code)
        if mtch:
            LOGGER.debug('code matches RE')
            self.type = mtch.group(1)
            self.decimal = ''
            self.size = 'D'

    def get_details(self):
        '''Get details from DB'''
        LOGGER.debug(
            'typ = %s size = %s decimal = %s',
            self.type,
            self.size,
            self.decimal)
        if self.size == 'D':
            details = StarTable.query.\
                filter_by(typ=self.type).\
                filter_by(size=self.size).\
                first()
        else:
            details = StarTable.query.\
                filter_by(typ=self.type).\
                filter_by(size=self.size).\
                filter_by(decimal=self.decimal).\
                first()
        LOGGER.debug('star = %s', details)
        if details:
            self.min_orbit = details.min_orbit
            self.hz_orbit = details.hz_orbit
            self.magnitude = details.magnitude
            self.luminosity = details.luminosity
            self.temperature = details.temperature
            self.radius = details.radius
            self.mass = details.mass
            self.int_orbit = details.int_orbit

    def calculate_hz_period(self):
        '''Calculate period of planet in HZ orbit'''
        if self.hz_orbit:
            orbit = OrbitTable.query.\
                filter_by(indx=self.hz_orbit).first()
            LOGGER.debug('orbit = %s', orbit)
            self.hz_period = round((orbit.au ** 3 / self.mass) ** 0.5, 3)
            LOGGER.debug('hz_period = %s', self.hz_period)

    def get_classification(self):
        '''Write canonical classification'''
        if self.type:
            self.classification = '{0}{1} {2}'.format(
                self.type, self.decimal, self.size)
