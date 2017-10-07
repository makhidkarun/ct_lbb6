'''planet.py'''

from flask import jsonify
from . import api
from . import errors
from ..main.planet import Planet


@api.route('/planet/<uwp>')
def get_uwp(uwp):
    '''Process UWP'''
    planet = Planet(uwp)
    if planet.uwp:
        return jsonify({
            'uwp': planet.uwp,
            'trade_classifications': planet.trade_classifications,
            'cloudiness': planet.cloudiness,
            'albedo': planet.albedo
        })
    else:
        return errors.bad_request('Invalid UWP {}'.format(uwp))


@api.route('/planet/<uwp>/trade_classifications')
@api.route('/star/<code>/orbit/<int:orbit_no>/trade_classifications')
def get_trade_classifications(uwp):
    '''Process trade classifications request'''
    planet = Planet(uwp)
    if planet.uwp:
        return jsonify({'trade_classifications': planet.trade_classifications})
    else:
        return errors.bad_request('Invalid UWP {}'.format(uwp))


@api.route('/planet/<uwp>/cloudiness')
@api.route('/star/<code>/orbit/<int:orbit_no>/cloudiness')
def get_cloudiness(uwp):
    '''Process clouduness request'''
    planet = Planet(uwp)
    if planet.uwp:
        return jsonify({'cloudiness': planet.cloudiness})
    else:
        return errors.bad_request('Invalid UWP {}'.format(uwp))


@api.route('/planet/<uwp>/albedo')
@api.route('/star/<code>/orbit/<int:orbit_no/albedo')
def get_albedo(uwp):
    '''Process clouduness request'''
    planet = Planet(uwp)
    if planet.uwp:
        return jsonify({'albedo': planet.albedo})
    else:
        return errors.bad_request('Invalid UWP {}'.format(uwp))


@api.route('/star/<code>/orbit/<int:orbit_no/temperature')
def get_temperature(uwp):
    '''Process clouduness request'''
    planet = Planet(uwp)
    if planet.uwp:
        return jsonify({'temperature': planet.temperature})
    else:
        return errors.bad_request('Invalid UWP {}'.format(uwp))
