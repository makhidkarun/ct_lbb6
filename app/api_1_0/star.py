'''star.py'''

import logging
from flask import jsonify
from . import api
from . import errors
from ..main.star import Star

LOGGER = logging.getLogger(__name__)


@api.route('/star/<code>')  # code should be of form <typ><decimal><size>
def get_star(code):
    '''Process star code'''
    star_json = {}
    star = Star(code)
    if star.type:
        star_json = {
            'typ': star.type,
            'decimal': star.decimal,
            'size': star.size,
            'min_orbit': star.min_orbit,
            'hz_orbit': star.hz_orbit,
            'magnitude': star.magnitude,
            'luminosity': star.luminosity,
            'temperature': star.temperature,
            'radius': star.radius,
            'mass': star.mass,
            'hz_period': star.hz_period
        }
        LOGGER.debug('Returning %s', jsonify(star_json).data)
        return jsonify(star_json)
    else:
        LOGGER.debug('Invalid star %s', code)
        return errors.bad_request('Invalid star {}'.format(code))


@api.route('/star/<code>/type')
def get_type(code):
    '''Process type'''
    star_json = {}
    star = Star(code)
    if star.type:
        star_json = {'typ': star.type}
        return jsonify(star_json)
    else:
        return errors.bad_request('Invalid star {}'.format(code))


@api.route('/star/<code>/decimal')
def get_decimal(code):
    '''Process decimal'''
    star_json = {}
    star = Star(code)
    if star.type:
        star_json = {'decimal': star.decimal}
        return jsonify(star_json)
    else:
        return errors.bad_request('Invalid star {}'.format(code))


@api.route('/star/<code>/size')
def get_size(code):
    '''Process size'''
    star_json = {}
    star = Star(code)
    if star.type:
        star_json = {'size': star.size}
        return jsonify(star_json)
    else:
        return errors.bad_request('Invalid star {}'.format(code))


@api.route('/star/<code>/min_orbit')
def get_min_orbit(code):
    '''Process min_orbit'''
    star_json = {}
    star = Star(code)
    if star.type:
        star_json = {'min_orbit': star.min_orbit}
        return jsonify(star_json)
    else:
        return errors.bad_request('Invalid star {}'.format(code))


@api.route('/star/<code>/hz_orbit')
def get_hz_orbit(code):
    '''Process hz_orbit'''
    star_json = {}
    star = Star(code)
    if star.type:
        star_json = {'hz_orbit': star.hz_orbit}
        return jsonify(star_json)
    else:
        return errors.bad_request('Invalid star {}'.format(code))


@api.route('/star/<code>/magnitude')
def get_magnitude(code):
    '''Process magnitude'''
    star_json = {}
    star = Star(code)
    if star.type:
        star_json = {'magnitude': star.magnitude}
        return jsonify(star_json)
    else:
        return errors.bad_request('Invalid star {}'.format(code))


@api.route('/star/<code>/luminosity')
def get_luminosity(code):
    '''Process luminosity'''
    star_json = {}
    star = Star(code)
    if star.type:
        star_json = {'luminosity': star.luminosity}
        return jsonify(star_json)
    else:
        return errors.bad_request('Invalid star {}'.format(code))


@api.route('/star/<code>/temperature')
def get_temperature(code):
    '''Process temperature'''
    star_json = {}
    star = Star(code)
    if star.type:
        star_json = {'temperature': star.temperature}
        return jsonify(star_json)
    else:
        return errors.bad_request('Invalid star {}'.format(code))


@api.route('/star/<code>/radius')
def get_radius(code):
    '''Process radius'''
    star_json = {}
    star = Star(code)
    if star.type:
        star_json = {'radius': star.radius}
        return jsonify(star_json)
    else:
        return errors.bad_request('Invalid star {}'.format(code))


@api.route('/star/<code>/mass')
def get_mass(code):
    '''Process mass'''
    star_json = {}
    star = Star(code)
    if star.type:
        star_json = {'mass': star.mass}
        return jsonify(star_json)
    else:
        return errors.bad_request('Invalid star {}'.format(code))


@api.route('/star/<code>/hz_period')
def get_hz_period(code):
    '''Process hz_period'''
    star_json = {}
    star = Star(code)
    if star.type:
        star_json = {'hz_period': star.hz_period}
        return jsonify(star_json)
    else:
        return errors.bad_request('Invalid star {}'.format(code))
