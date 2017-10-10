'''test_star_api.py'''

import unittest
import logging
import app.api_1_0.star as Api
from flask import jsonify

LOGGER = logging.getLogger(__name__)


class TestStarAPI(unittest.TestCase):
    '''star API unit tests'''
    def test_get_star(self):
        '''API: Star - test get_star()'''
        expected = jsonify({
            'typ': 'K',
            'decimal': 2,
            'size': 'IV',
            'min_orbit': 0,
            'hz_orbit': 5,
            'magnitude': 2.34,
            'luminosity': 6.802,
            'temperature': 4276,
            'radius': 6.7,
            'mass': 2.98,
            'hz_period': 2.714
        })
        received = Api.get_star('K2IV')
        self.assertTrue(expected.data == received.data)
        self.assertTrue(received.status_code == 200)

    def test_get_type(self):
        '''API: Star - test get_type()'''
        expected = jsonify({'typ': 'M'})
        received = Api.get_type('M2II')
        self.assertTrue(expected.data == received.data)
        self.assertTrue(received.status_code == 200)

    def test_get_decimal(self):
        '''API: Star - test get_decimal()'''
        expected = jsonify({'decimal': 3})
        received = Api.get_decimal('K3V')
        self.assertTrue(expected.data == received.data)
        self.assertTrue(received.status_code == 200)

    def test_get_decimal_dwarf(self):
        '''API: Star - test get_decimal() for dwarf'''
        expected = jsonify({'decimal': ''})
        received = Api.get_decimal('KD')
        LOGGER.debug('Received %s', received.data)
        self.assertTrue(expected.data == received.data)
        self.assertTrue(received.status_code == 200)

    def test_get_size(self):
        '''API: Star - test get_size()'''
        expected = jsonify({'size': 'V'})
        received = Api.get_size('G2V')
        self.assertTrue(expected.data == received.data)
        self.assertTrue(received.status_code == 200)

    def test_get_min_orbit(self):
        '''API: Star - test get_min_orbit()'''
        expected = jsonify({'min_orbit': 8})
        received = Api.get_min_orbit('B0Ia')
        self.assertTrue(expected.data == received.data)
        self.assertTrue(received.status_code == 200)

    def test_get_hz_orbit(self):
        '''API: Star - test get_hz_orbit()'''
        expected = jsonify({'hz_orbit': 13})
        received = Api.get_hz_orbit('B0Ia')
        self.assertTrue(expected.data == received.data)
        self.assertTrue(received.status_code == 200)

    def test_get_magnitude(self):
        '''API: Star - test get_magnitude()'''
        expected = jsonify({'magnitude': 7.4})
        received = Api.get_magnitude('K5V')
        self.assertTrue(expected.data == received.data)
        self.assertTrue(received.status_code == 200)

    def test_get_luminosity(self):
        '''API: Star - test get_luminosity()'''
        expected = jsonify({'luminosity': 5.22})
        received = Api.get_luminosity('G4IV')
        self.assertTrue(expected.data == received.data)
        self.assertTrue(received.status_code == 200)

    def test_get_temperature(self):
        '''API: Star - test get_temperature()'''
        expected = jsonify({'temperature': 5340})
        received = Api.get_temperature('G4IV')
        self.assertTrue(expected.data == received.data)
        self.assertTrue(received.status_code == 200)

    def test_get_radius(self):
        '''API: Star - test get_radius()'''
        expected = jsonify({'radius': 2.74})
        received = Api.get_radius('G4IV')
        self.assertTrue(expected.data == received.data)
        self.assertTrue(received.status_code == 200)

    def test_get_mass(self):
        '''API: Star - test get_mass()'''
        expected = jsonify({'mass': 1.14})
        received = Api.get_mass('F8V')
        self.assertTrue(expected.data == received.data)
        self.assertTrue(received.status_code == 200)

    def test_get_hz_period(self):
        '''API: Star - test get_hz_period()'''
        expected = jsonify({'hz_period': 8.513})
        received = Api.get_hz_period('A7V')
        self.assertTrue(expected.data == received.data)
        self.assertTrue(received.status_code == 200)

    def test_get_hz_period_dwarf(self):
        '''API: Star - test get_hz_period() - dwarf'''
        expected = jsonify({'hz_period': None})
        received = Api.get_hz_period('MD')
        self.assertTrue(expected.data == received.data)
        self.assertTrue(received.status_code == 200)


class TestStarAPIFail(unittest.TestCase):
    '''star API unit tests - failures'''
    code = 'Q2II'
    expected = jsonify({
        'error': 'bad request',
        'message': 'Invalid star {}'.format(code)})

    def test_get_star_fail(self):
        '''API: Star - test get_star() - fail'''
        received = Api.get_star(self.code)
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_type_fail(self):
        '''API: Star - test get_type() - fail'''
        received = Api.get_type(self.code)
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_decimal(self):
        '''API: Star - test get_decimal()'''
        received = Api.get_decimal(self.code)
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_size(self):
        '''API: Star - test get_size()'''
        received = Api.get_size(self.code)
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_min_orbit(self):
        '''API: Star - test get_min_orbit()'''
        received = Api.get_min_orbit(self.code)
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_hz_orbit(self):
        '''API: Star - test get_hz_orbit()'''
        received = Api.get_hz_orbit(self.code)
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_magnitude(self):
        '''API: Star - test get_magnitude()'''
        received = Api.get_magnitude(self.code)
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_luminosity(self):
        '''API: Star - test get_luminosity()'''
        received = Api.get_luminosity(self.code)
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_temperature(self):
        '''API: Star - test get_temperature()'''
        received = Api.get_temperature(self.code)
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_radius(self):
        '''API: Star - test get_radius()'''
        received = Api.get_radius(self.code)
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_mass(self):
        '''API: Star - test get_mass()'''
        received = Api.get_mass(self.code)
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_hz_period(self):
        '''API: Star - test get_hz_period()'''
        received = Api.get_hz_period(self.code)
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)
