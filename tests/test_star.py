'''test_star.py'''

import unittest
import logging
from app.main.star import Star

LOGGER = logging.getLogger(__name__)
# LOGGER.setLevel(logging.DEBUG)


class TestStar(unittest.TestCase):
    '''Star tests'''
    def test_validate_valid_code(self):
        '''Star - Test validation: valid code'''
        star = Star('G2 V')
        LOGGER.debug('Type = %s', star.type)
        LOGGER.debug('Decimal = %s', star.decimal)
        LOGGER.debug('Size = %s', star.size)
        self.assertTrue(star.type == 'G')
        self.assertTrue(star.decimal == 2)
        self.assertTrue(star.size == 'V')

    def test_validate_m_iv(self):
        '''Star - test IV->V for M'''
        star = Star('M2 IV')
        LOGGER.debug('Type = %s', star.type)
        LOGGER.debug('Decimal = %s', star.decimal)
        LOGGER.debug('Size = %s', star.size)
        self.assertTrue(star.size == 'V')

    def test_validate_k_iv(self):
        '''Star - test IV->V for K5-9'''
        star = Star('K7 IV')
        LOGGER.debug('Type = %s', star.type)
        LOGGER.debug('Decimal = %s', star.decimal)
        LOGGER.debug('Size = %s', star.size)
        self.assertTrue(star.size == 'V')
        star = Star('K2 IV')
        LOGGER.debug('Type = %s', star.type)
        LOGGER.debug('Decimal = %s', star.decimal)
        LOGGER.debug('Size = %s', star.size)
        self.assertTrue(star.size == 'IV')

    def test_validate_bf_vi(self):
        '''Star - test Vi->V for B0-F4'''
        star = Star('B3 VI')
        self.assertTrue(star.size == 'V')
        star = Star('F2 VI')
        self.assertTrue(star.size == 'V')
        star = Star('F7 VI')
        self.assertTrue(star.size == 'VI')

    def test_validate_d_with_space(self):
        '''Star - test valiation: dwarf (code =" G D")'''
        star = Star('G D')
        self.assertTrue(star.type == 'G')
        self.assertTrue(star.size == 'D')
        self.assertTrue(star.decimal == '')

    def test_validate_d_without_space(self):
        '''Star - test valiation: dwarf (code =" GD")'''
        star = Star('GD')
        self.assertTrue(star.type == 'G')
        self.assertTrue(star.size == 'D')
        self.assertTrue(star.decimal == '')

    def test_get_details(self):
        '''Star - test get_details()'''
        star = Star('G2 V')
        self.assertTrue(star.min_orbit == 0)
        self.assertTrue(star.hz_orbit == 3)
        self.assertTrue(star.magnitude == 4.82)
        self.assertTrue(star.luminosity == 0.994)
        self.assertTrue(star.temperature == 5800)
        self.assertTrue(star.radius == 0.98)
        self.assertTrue(star.mass == 1.0)

    def test_hz_orbit_hz_exists(self):
        '''Star - test hz_orbit() where there is a HZ'''
        star = Star('G2 V')
        self.assertTrue(star.hz_period == 1.0)

    def test_hz_orbit_no_hz(self):
        '''Star - test hz_orbit() where there is no HZ'''
        star = Star('M2 V')
        self.assertTrue(star.hz_period is None)
