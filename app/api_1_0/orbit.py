'''orbit.py'''

from flask import jsonify, current_app
from . import api
from . import errors
from ..main.star import Star
from ..main.orbit import Orbit


@api.route('/star/<code>/orbit')
def return_orbit_star(code):
    '''Return min_orbit, hz_orbit, hz_period'''
    star = Star(code)
    current_app.logger.debug('star classification = %s', star.classification)
    if star.classification:
        current_app.logger.debug('Star and orbit valid')
        return jsonify({
            'min_orbit': star.min_orbit,
            'hz_orbit': star.hz_orbit,
            'hz_period': star.hz_period
        })
    else:
        return errors.bad_request('Invalid star {}'.format(code))


@api.route('/star/<code>/orbit/<int:orbit_no>')
def return_orbit_basic_details(code, orbit_no):
    '''Return basic orbit details'''
    star = Star(code)
    orbit = Orbit(star, orbit_no)
    current_app.logger.debug('star classification = %s', star.classification)
    current_app.logger.debug('orbit_no = %s', orbit_no)
    if star.classification and orbit.orbit_no is not None:
        current_app.logger.debug('Star and orbit valid')
        return jsonify({
            'period': orbit.period,
            'angular_diameter_sun': orbit.angular_dia_sun,
            'angular_diameter_deg': orbit.angular_dia_deg,
            'au': orbit.au,
            'mkm': orbit.mkm
        })
    else:
        return errors.bad_request(
            'Invalid star {} or orbit {}'.format(code, orbit_no))


@api.route(('/star/<code>/orbit/<int:orbit_no>/period'))
def return_orbit_period(code, orbit_no):
    '''Return orbit period'''
    star = Star(code)
    orbit = Orbit(star, orbit_no)
    current_app.logger.debug('star classification = %s', star.classification)
    current_app.logger.debug('orbit_no = %s', orbit_no)
    if star.classification and orbit.orbit_no is not None:
        current_app.logger.debug('Star and orbit valid')
        return jsonify({'period': orbit.period})
    else:
        return errors.bad_request(
            'Invalid star {} or orbit {}'.format(code, orbit_no))


@api.route(('/star/<code>/orbit/<int:orbit_no>/angular_diameter'))
def return_orbit_angular_diameter(code, orbit_no):
    '''Return orbit angular_diameter'''
    star = Star(code)
    orbit = Orbit(star, orbit_no)
    current_app.logger.debug('star classification = %s', star.classification)
    current_app.logger.debug('orbit_no = %s', orbit_no)
    if star.classification and orbit.orbit_no is not None:
        current_app.logger.debug('Star and orbit valid')
        return jsonify({
            'angular_diameter_deg': orbit.angular_dia_deg,
            'angular_diameter_sun': orbit.angular_dia_sun})
    else:
        return errors.bad_request(
            'Invalid star {} or orbit {}'.format(code, orbit_no))


@api.route(('/star/<code>/orbit/<int:orbit_no>/radius'))
def return_orbit_radius(code, orbit_no):
    '''Return orbit radius'''
    star = Star(code)
    orbit = Orbit(star, orbit_no)
    current_app.logger.debug('star classification = %s', star.classification)
    current_app.logger.debug('orbit_no = %s', orbit_no)
    if star.classification is not None and orbit.orbit_no is not None:
        current_app.logger.debug('Star and orbit valid')
        return jsonify({
            'au': orbit.au,
            'mkm': orbit.mkm})
    else:
        return errors.bad_request(
            'Invalid star {} or orbit {}'.format(code, orbit_no))
