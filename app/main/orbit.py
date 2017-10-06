'''orbit.py'''

import logging
from math import atan2, pi
from ..models import OrbitTable

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


class Orbit(object):
    '''Orbit class'''
    def __init__(self, star, orbit_no=0):
        self.star = star
        self.orbit_no = orbit_no
        self.au = 0
        self.mkm = 0
        self.period = 0
        self.angular_dia_deg = 0
        self.angular_dia_sun = 0
        self.get_radius()
        self.determine_period()
        self.determine_angular_diameter()

    def determine_period(self):
        '''Determine orbital period - need orbit radius, stellar mass'''
        self.period = (self.au ** 3 / self.star.mass) ** 0.5
        LOGGER.debug('period = %s', self.period)

    def determine_angular_diameter(self):
        '''Determine angular diameter of star as seen from this orbit'''
        # a = 2*arctan(Dstellar / (2 * R))
        # Convert from solar dia to Mkm (Dsun = 1.3914 Mkm)
        stellar_dia = self.star.radius * 1.3914
        LOGGER.debug('stellar dia = %s Mkm', stellar_dia)
        LOGGER.debug('orbital rad = %s Mkm', self.mkm)
        self.angular_dia_deg = atan2(stellar_dia, self.mkm) * 180 / pi
        # Sun's angular diameter from earth orbit ~ 0.522 deg
        self.angular_dia_sun = self.angular_dia_deg / 0.522
        LOGGER.debug(
            'angular dia = %s (%sx the sun from earth',
            self.angular_dia_deg,
            self.angular_dia_sun)

    def get_radius(self):
        '''Get orbit radius from OrbitTable'''
        details = OrbitTable.query.\
            filter_by(indx=self.orbit_no).\
            first()
        LOGGER.debug('orbit = %s', details)
        self.au = details.au
        self.mkm = details.mkm
