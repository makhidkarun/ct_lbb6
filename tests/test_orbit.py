'''test_orbit.py'''

import unittest
import logging

from app.main.star import Star
from app.main.orbit import Orbit

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


class TestOrbit(unittest.TestCase):
    ''' Orbit unit tests'''
    star = Star('G2 V')
    orbit = Orbit(star, 3)

    def test_period(self):
        '''Orbit - test orbital period calculation'''
        LOGGER.debug('orbit.period = %s', self.orbit.period)
        self.assertTrue(self.orbit.period == 1.0)

    def test_angular_diameter(self):
        '''Orbit - test angular diameter calculation'''
        LOGGER.debug(
            'angular dia = %s (%sx the sun from earth',
            self.orbit.angular_dia_deg,
            self.orbit.angular_dia_sun)
        self.assertAlmostEqual(self.orbit.angular_dia_deg, 0.5, 1)
        self.assertAlmostEqual(self.orbit.angular_dia_sun, 1.0, 1)

    def test_radius(self):
        '''Orbit - test radius lookup'''
        self.assertTrue(self.orbit.au == 1)
        self.assertTrue(self.orbit.mkm == 149.6)
