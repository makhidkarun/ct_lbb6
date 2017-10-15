'''test_client.py'''

import unittest
from flask import url_for, jsonify, request
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

    def test_query(self):
        '''Test index page with query'''
        response = self.client.post(
            url_for('main.index'),
            data={
                'star': 'F7V',
                'orbit': '3',
                'planet': 'A4307BA-B'
            })
        data = response.get_data(as_text=True)
        self.assertTrue('Star F7 V' in data)
        self.assertTrue(response.status_code == 200)
