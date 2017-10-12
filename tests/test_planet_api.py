'''test_planet_api.py'''

import unittest
import logging
import app.api_1_0.planet as Api
from flask import jsonify

LOGGER = logging.getLogger(__name__)


class TestPlanetAPI(unittest.TestCase):
    '''Planet unit tests'''
    def test_get_uwp(self):
        '''API: Planet - test get_uwp()'''
        pass

    def test_get_trade_classifications(self):
        '''API: Planet - test get_trade_classifications()'''
        pass

    def test_get_cloudiness(self):
        '''API: Planet - test get_cloudiness()'''
        pass

    def test_get_albedo(self):
        '''API: Planet - test get_albedo()'''
        pass

    def test_get_temperature(self):
        '''API: Planet - test get_temperature()'''
        pass


class TestPlanetAPIFail(unittest.TestCase):
    '''Planet unit tests - failures'''
    uwp = 'ZZ9ZZA0-0'
    expected = jsonify({
        'error': 'bad request',
        'message': 'Invalid UWP {}'.format(uwp)})

    def test_get_uwp_fail(self):
        '''API: Planet - test get_uwp() - fail'''
        received = Api.get_uwp(self.uwp)
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_trade_class_fail(self):
        '''API: Planet - test get_trade_classifications() - fail'''
        received = Api.get_trade_classifications(self.uwp)
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_cloudiness_fail(self):
        '''API: Planet - test get_cloudiness() - fail'''
        received = Api.get_cloudiness(self.uwp)
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_albedo_fail(self):
        '''API: Planet - test get_albedo() - fail'''
        received = Api.get_albedo(self.uwp)
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_temperature_fail(self):
        '''API: Planet - test get_temperature() - fail'''
        code = 'FD'
        orbit_no = 3
        received = Api.get_base_temperature(self.uwp, code, orbit_no)
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)
