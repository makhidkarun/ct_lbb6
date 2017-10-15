'''test_planet_api.py'''

import unittest
import logging
import app.api_1_0.planet as Api
from flask import jsonify, url_for
from app import create_app, db

LOGGER = logging.getLogger(__name__)


class TestPlanetAPI(unittest.TestCase):
    '''Planet unit tests'''
    star_classification = 'G2V'
    orbit_no = 3
    planet_uwp = 'A788587-9'
    api_headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    def setUp(self):
        '''Setup'''
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        '''Teardown'''
        db.session.remove()
        self.app_context.pop()

    def test_get_uwp(self):
        '''API: Planet - test get_uwp()'''
        response = self.client.get(
            url_for('api.get_uwp', uwp=self.planet_uwp),
            content_type='application/json')
        expected = jsonify({
            "albedo": {
                "max": 0.586,
                "min": 0.293
            },
            "cloudiness": 0.6,
            "trade_classifications": [
                "Ag",
                "Ni"
            ],
            "uwp": "A788587-9"
        })
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_get_uwp_star_orbit(self):
        '''Test /star/<code>/orbit/<int:orbit_no>/planet/<uwp>'''
        response = self.client.get(
            url_for(
                'api.get_uwp_star',
                code=self.star_classification,
                orbit_no=self.orbit_no,
                uwp=self.planet_uwp),
            content_type='application/json')
        expected = jsonify({
            "albedo": {
                "max": 0.586,
                "min": 0.293
            },
            "cloudiness": 0.6,
            "trade_classifications": [
                "Ag",
                "Ni"
            ],
            "uwp": "A788587-9"
        })
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_get_trade_classifi_star(self):
        '''API: Planet - test get_trade_classifications()'''
        response = self.client.get(
            url_for(
                'api.get_trade_classifications_star',
                uwp=self.planet_uwp,
                orbit_no=self.orbit_no,
                code=self.star_classification),
            content_type='application/json')
        expected = jsonify({
            "trade_classifications": [
                "Ag",
                "Ni"
            ],
        })
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_get_trade_classifications(self):
        '''API: Planet - test get_trade_classifications()'''
        response = self.client.get(
            url_for('api.get_trade_classifications', uwp=self.planet_uwp),
            content_type='application/json')
        expected = jsonify({
            "trade_classifications": [
                "Ag",
                "Ni"
            ],
        })
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_get_cloudiness(self):
        '''API: Planet - test get_cloudiness()'''
        response = self.client.get(
            url_for('api.get_cloudiness', uwp=self.planet_uwp),
            content_type='application/json')
        expected = jsonify({"cloudiness": 0.6})
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_get_cloudiness_star(self):
        '''API: Planet - test get_cloudiness()'''
        response = self.client.get(
            url_for(
                'api.get_cloudiness_star',
                uwp=self.planet_uwp,
                orbit_no=self.orbit_no,
                code=self.star_classification),
            content_type='application/json')
        expected = jsonify({"cloudiness": 0.6})
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_get_albedo(self):
        '''API: Planet - test get_albedo()'''
        response = self.client.get(
            url_for('api.get_albedo', uwp=self.planet_uwp),
            content_type='application/json')
        expected = jsonify({
            "albedo": {
                "max": 0.586,
                "min": 0.293
            }
        })
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_get_albedo_star(self):
        '''API: Planet - test get_albedo()'''
        response = self.client.get(
            url_for(
                'api.get_albedo_star',
                uwp=self.planet_uwp,
                orbit_no=self.orbit_no,
                code=self.star_classification),
            content_type='application/json')
        expected = jsonify({
            "albedo": {
                "max": 0.586,
                "min": 0.293
            }
        })
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_get_temperature(self):
        '''API: Planet - test get_temperature()'''
        response = self.client.get(
            url_for(
                'api.get_base_temperature',
                uwp=self.planet_uwp,
                orbit_no=self.orbit_no,
                code=self.star_classification),
            content_type='application/json')
        expected = jsonify({
            "temperature": {
                "max": 303.644,
                "min": 177.806
            }
        })
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)


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
