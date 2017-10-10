'''orbit.py'''

import logging
from math import atan2, pi
from ..models import OrbitTable

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


class Orbit(object):
    '''Orbit class'''
    def __init__(self, star, orbit_no=None):
        self.star = star
        self.orbit_no = None
        self.au = 0
        self.mkm = 0
        self.period = 0
        self.angular_dia_deg = 0
        self.angular_dia_sun = 0
        LOGGER.debug('orbit_no = %s', orbit_no)
        LOGGER.debug('type(orbit_no) = %s', type(orbit_no))
        self.get_radius(orbit_no)
        self.determine_period()
        self.determine_angular_diameter()

    def determine_period(self):
        '''Determine orbital period - need orbit radius, stellar mass'''
        if self.star and self.orbit_no is not None:
            self.period = round((self.au ** 3 / self.star.mass) ** 0.5, 3)
            LOGGER.debug('period = %s', self.period)

    def determine_angular_diameter(self):
        '''Determine angular diameter of star as seen from this orbit'''
        # a = 2*arctan(Dstellar / (2 * R))
        # Convert from solar dia to Mkm (Dsun = 1.3914 Mkm)
        if self.star and self.orbit_no is not None:
            stellar_dia = self.star.radius * 1.3914
            LOGGER.debug('stellar dia = %s Mkm', stellar_dia)
            LOGGER.debug('orbital rad = %s Mkm', self.mkm)
            self.angular_dia_deg = round(
                atan2(stellar_dia, self.mkm) * 180 / pi,
                3)
            # Sun's angular diameter from earth orbit ~ 0.522 deg
            self.angular_dia_sun = round(self.angular_dia_deg / 0.522, 3)
            LOGGER.debug(
                'angular dia = %s degrees (%sx the sun from earth)',
                self.angular_dia_deg,
                self.angular_dia_sun)

    def get_radius(self, orbit_no):
        '''Get orbit radius from OrbitTable'''
        if self.star and orbit_no is not None:
            details = OrbitTable.query.\
                filter_by(indx=orbit_no).\
                first()

            LOGGER.debug('orbit details = %s', details)
            if details:
                self.orbit_no = orbit_no
                self.au = details.au
                self.mkm = details.mkm
                # Tag infeasible orbits
                if orbit_no <= self.star.min_orbit:
                    self.orbit_no = '{0} (orbit too close to star)'.format(
                        orbit_no)
                if self.star.int_orbit is not None:
                    LOGGER.debug('Star has potential internal orbits')
                    if orbit_no <= self.star.int_orbit:
                        self.orbit_no = '{0} (orbit within star)'.format(
                            orbit_no)
