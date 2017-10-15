'''test_orbit_api.py'''

import unittest
import logging
from flask import jsonify, url_for
from app import create_app, db

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


class TestOrbitApi(unittest.TestCase):
    '''Test orbit API calls'''
    star_text = 'G2V'
    orbit_no = 3

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
            url_for(endpoint, code=self.star_text, orbit_no=self.orbit_no))

    def test_orbit_basic_details(self):
        '''Test /<star>/orbit/<orbit>'''
        expected = jsonify({
            "angular_diameter_deg": 0.522,
            "angular_diameter_sun": 1.0,
            "au": 1,
            "mkm": 149.6,
            "period": 1.0
        })
        received = self.api_query('api.return_orbit_basic_details')
        self.assertTrue(received.data == expected.data)
        self.assertTrue(received.status_code == 200)

    def test_orbit_period(self):
        '''Test /<star>/orbit/<orbit>/period'''
        expected = jsonify({"period": 1.0})
        received = self.api_query('api.return_orbit_period')
        self.assertTrue(received.data == expected.data)
        self.assertTrue(received.status_code == 200)

    def test_orbit_angular_diameter(self):
        '''test /<star>/orbit/<orbit>/angular_diameter'''
        expected = jsonify({
            "angular_diameter_deg": 0.522,
            "angular_diameter_sun": 1.0,
        })
        received = self.api_query('api.return_orbit_angular_diameter')
        self.assertTrue(received.data == expected.data)
        self.assertTrue(received.status_code == 200)

    def test_orbit_radius(self):
        '''Test /<star>/orbit/<orbit>/radius'''
        expected = jsonify({
            "au": 1,
            "mkm": 149.6,
        })
        received = self.api_query('api.return_orbit_radius')
        self.assertTrue(received.data == expected.data)
        self.assertTrue(received.status_code == 200)

    def test_orbit_star(self):
        '''Test /<star>/orbit>'''
        expected = jsonify({
            "hz_orbit": 3,
            "hz_period": 1.0,
            "min_orbit": 0
        })
        received = self.api_query('api.return_orbit_star')
        self.assertTrue(received.data == expected.data)
        self.assertTrue(received.status_code == 200)


class TestOrbitApiFail(unittest.TestCase):
    '''Test orbit API calls'''
    star_text = 'G2P'
    orbit_no = 3
    msg = 'Invalid star %s or orbit %s' % (star_text, orbit_no)
    expected = jsonify({'error': 'bad request', 'message': msg})

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
            url_for(endpoint, code=self.star_text, orbit_no=self.orbit_no))

    def test_orbit_basic_details(self):
        '''Test /<star>/orbit/<orbit>'''
        received = self.api_query('api.return_orbit_basic_details')
        self.assertTrue(received.data == self.expected.data)
        self.assertTrue(received.status_code == 400)

    def test_orbit_period(self):
        '''Test /<star>/orbit/<orbit>/period'''
        received = self.api_query('api.return_orbit_period')
        self.assertTrue(received.data == self.expected.data)
        self.assertTrue(received.status_code == 400)

    def test_orbit_angular_diameter(self):
        '''test /<star>/orbit/<orbit>/angular_diameter'''
        received = self.api_query('api.return_orbit_angular_diameter')
        self.assertTrue(received.data == self.expected.data)
        self.assertTrue(received.status_code == 400)

    def test_orbit_radius(self):
        '''Test /<star>/orbit/<orbit>/radius'''
        received = self.api_query('api.return_orbit_radius')
        self.assertTrue(received.data == self.expected.data)
        self.assertTrue(received.status_code == 400)

    def test_orbit_star(self):
        '''Test /<star>/orbit>'''
        received = self.api_query('api.return_orbit_star')
        msg = 'Invalid star %s' % self.star_text
        expected = jsonify({'error': 'bad request', 'message': msg})
        LOGGER.debug('expected.data = %s', expected.data)
        LOGGER.debug('received.data = %s', received.data)
        self.assertTrue(received.data == expected.data)
        self.assertTrue(received.status_code == 400)
