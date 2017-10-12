'''test_star_api.py'''

import unittest
import logging
import app.api_1_0.star as Api
from flask import jsonify, url_for
from app import create_app, db

LOGGER = logging.getLogger(__name__)


class TestStarAPI(unittest.TestCase):
    '''star API unit tests'''
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

    def test_star(self):
        '''Test /ct/lbb6/star/<classification>'''
        response = self.client.get(
            url_for('api.get_star', code=self.star_classification),
            content_type='application/json')
        expected = jsonify({
            "decimal": 2,
            "hz_orbit": 3,
            "hz_period": 1.0,
            "luminosity": 0.994,
            "magnitude": 4.82,
            "mass": 1.0,
            "min_orbit": 0,
            "radius": 0.98,
            "size": "V",
            "temperature": 5800,
            "typ": "G"
        })
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_star_type(self):
        '''Test /<star>/type'''
        response = self.client.get(
            url_for('api.get_type', code=self.star_classification),
            content_type='application/json')
        expected = jsonify({"typ": "G"})
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_star_decimal(self):
        '''Test /<star>/decimal'''
        response = self.client.get(
            url_for('api.get_decimal', code=self.star_classification),
            content_type='application/json')
        expected = jsonify({"decimal": 2})
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_size(self):
        '''Test /<star>/size'''
        response = self.client.get(
            url_for('api.get_size', code=self.star_classification),
            content_type='application/json')
        expected = jsonify({"size": "V"})
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_min_orbit(self):
        '''Test /<star>/min_orbit'''
        response = self.client.get(
            url_for('api.get_min_orbit', code=self.star_classification),
            content_type='application/json')
        expected = jsonify({"min_orbit": 0})
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_hz_orbit(self):
        '''Test /<star>/hz_orbit'''
        response = self.client.get(
            url_for('api.get_hz_orbit', code=self.star_classification),
            content_type='application/json')
        expected = jsonify({"hz_orbit": 3})
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_magnitude(self):
        '''Test /<star>/magnitude'''
        response = self.client.get(
            url_for('api.get_magnitude', code=self.star_classification),
            content_type='application/json')
        expected = jsonify({"magnitude": 4.82})
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_luminosity(self):
        '''Test /<star>/luminosity'''
        response = self.client.get(
            url_for('api.get_luminosity', code=self.star_classification),
            content_type='application/json')
        expected = jsonify({"luminosity": 0.994})
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_temperature(self):
        '''Test /<star>/temperature'''
        response = self.client.get(
            url_for('api.get_temperature', code=self.star_classification),
            content_type='application/json')
        expected = jsonify({"temperature": 5800})
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_radius(self):
        '''Test /<star>/radius'''
        response = self.client.get(
            url_for('api.get_radius', code=self.star_classification),
            content_type='application/json')
        expected = jsonify({"radius": 0.98})
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_mass(self):
        '''Test <star>/mass'''
        response = self.client.get(
            url_for('api.get_mass', code=self.star_classification),
            content_type='application/json')
        expected = jsonify({"mass": 1.0})
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)

    def test_hz_period(self):
        '''Test /<star>/hz_period'''
        response = self.client.get(
            url_for('api.get_hz_period', code=self.star_classification),
            content_type='application/json')
        expected = jsonify({"hz_period": 1.0})
        self.assertTrue(response.data == expected.data)
        self.assertTrue(response.status_code == 200)


class TestStarAPIFail(unittest.TestCase):
    '''star API unit tests - failures'''
    code = 'Q2II'
    expected = jsonify({
        'error': 'bad request',
        'message': 'Invalid star {}'.format(code)})

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

    def api_query(self, endpoint):
        '''Generic API query'''
        return self.client.get(
            url_for(endpoint, code=self.code))

    def test_get_star_fail(self):
        '''Test /star/<code> - fail'''
        received = self.api_query('api.get_star')
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_type_fail(self):
        '''Test /star/<code>/type - fail'''
        received = self.api_query('api.get_type')
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_decimal(self):
        '''Test /star/<code>/decimal - fail'''
        received = self.api_query('api.get_decimal')
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_size(self):
        '''Test /star/<code>/size - fail'''
        received = self.api_query('api.get_size')
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_min_orbit(self):
        '''Test /star/<code>/min_orbit - fail'''
        received = self.api_query('api.get_min_orbit')
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_hz_orbit(self):
        '''Test /star/<code>/hz_orbit - fail'''
        received = self.api_query('api.get_hz_orbit')
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_magnitude(self):
        '''Test /star/<code>/magnitude - fail'''
        received = self.api_query('api.get_magnitude')
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_luminosity(self):
        '''Test /star/code/luminosity - fail'''
        received = self.api_query('api.get_luminosity')
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_temperature(self):
        '''Test /star/<code>/temperature - fail'''
        received = self.api_query('api.get_temperature')
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_radius(self):
        '''Test /star/<code>/radius - fail'''
        received = self.api_query('api.get_radius')
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_mass(self):
        '''Test /star/<code>/mass - fail'''
        received = self.api_query('api.get_mass')
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)

    def test_get_hz_period(self):
        '''Test /star/<code>/hz_period'''
        received = self.api_query('api.get_hz_period')
        self.assertTrue(self.expected.data == received.data)
        self.assertTrue(received.status_code == 400)
