'''test_client.py'''

import unittest
from flask import url_for, jsonify
from app import create_app, db


class FlaskClientTestCase(unittest.TestCase):
    '''Flask test client'''
    def setUp(self):
        '''Setup'''
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        '''Teardown'''
        db.session.remove()
        self.app_context.pop()

    def test_index(self):
        '''Test index page'''
        response = self.client.get(url_for('main.index'))
        self.assertTrue(b'LBB6 Star/Orbit/Planet' in response.data)
