'''test_planet.py'''

import unittest
import logging
from app.main.planet import Planet
from app.main.star import Star
from app.main.orbit import Orbit

LOGGER = logging.getLogger(__name__)


class TestPlanet(unittest.TestCase):
    '''Planet unit tests'''
    def test_uwp_valid(self):
        '''Planet - test valid UWP'''
        uwp = 'A788899-A'
        planet = Planet(uwp)
        self.assertTrue(planet.uwp == uwp)
        self.assertTrue(planet.starport == 'A')
        self.assertTrue(planet.size == '7')
        self.assertTrue(planet.atmosphere == '8')
        self.assertTrue(planet.hydrographics == '8')
        self.assertTrue(planet.population == '8')
        self.assertTrue(planet.government == '9')
        self.assertTrue(planet.lawlevel == '9')
        self.assertTrue(planet.techlevel == 'A')

    def test_uwp_invalid(self):
        '''Planet - test invalid UWP'''
        uwp = 'ZZ9ZZA0-0'
        planet = Planet(uwp)
        self.assertTrue(planet.uwp is None)

    def test_trade_codes(self):
        '''Planet - test trade classifications'''
        planet = Planet('A788899-A')
        LOGGER.debug('uwp: %s', planet.uwp)
        LOGGER.debug(
            'trade_classifications = %s',
            planet.trade_classifications)
        self.assertTrue(planet.trade_classifications == ['Ri'])

    def test_cloudiness(self):
        '''Planet - test cloudiness calculation'''
        planet = Planet('A788899-A')
        self.assertTrue(planet.cloudiness == 0.6)

    def test_albedo(self):
        '''Planet - test albedo calculation'''
        planet = Planet('A788899-A')
        self.assertTrue(planet.albedo['min'] == 0.292568)
        self.assertTrue(planet.albedo['max'] == 0.586)

    def test_albedo_de(self):
        '''Planet - test albedo calculation - desert world'''
        planet = Planet('D640000-0')
        self.assertTrue(planet.albedo['min'] == 0.2)
        self.assertTrue(planet.albedo['max'] == 0.2)

    def test_albedo_ic(self):
        '''Planet - test albedo calculation - ice-capped world'''
        planet = Planet('C415000-0')
        self.assertTrue(planet.albedo['min'] == 0.2175)
        self.assertTrue(planet.albedo['max'] == 0.2175)

    def test_temperature(self):
        '''Planet - test temperature calculation'''
        star = Star('F7V')
        orbit = Orbit(star, 4)
        planet = Planet('A788899-A', orbit=orbit, star=star)
        self.assertAlmostEquals(planet.temperature['max'], 348.7, 1)
        self.assertAlmostEquals(planet.temperature['min'], 204.1, 1)
