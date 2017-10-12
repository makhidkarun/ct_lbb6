'''planet.py'''

from flask import jsonify
from . import api
from . import errors
from ..main.planet import Planet
from ..main.star import Star
from ..main.orbit import Orbit


@api.route('/star/<code>/orbit/<int:orbit_no>/planet/<uwp>')
def get_uwp_star(uwp, code, orbit_no):
    '''Process UWP via star route'''
    del code
    del orbit_no
    return get_uwp(uwp)


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


@api.route(
    '/star/<code>/orbit/<int:orbit_no>/planet/<uwp>/trade_classifications')
def get_trade_classifications_star(code, orbit_no, uwp):
    '''Get trade classifications via star route'''
    del code
    del orbit_no
    return get_trade_classifications(uwp)


@api.route('/planet/<uwp>/trade_classifications')
def get_trade_classifications(uwp):
    '''Process trade classifications request'''
    planet = Planet(uwp)
    if planet.uwp:
        return jsonify({'trade_classifications': planet.trade_classifications})
    else:
        return errors.bad_request('Invalid UWP {}'.format(uwp))


@api.route('/star/<code>/orbit/<int:orbit_no>/planet/<uwp>/cloudiness')
def get_cloudiness_star(code, orbit_no, uwp):
    '''Get cloudiness via star route'''
    del code
    del orbit_no
    return get_cloudiness(uwp)


@api.route('/planet/<uwp>/cloudiness')
def get_cloudiness(uwp):
    '''Process clouduness request'''
    planet = Planet(uwp)
    if planet.uwp:
        return jsonify({'cloudiness': planet.cloudiness})
    else:
        return errors.bad_request('Invalid UWP {}'.format(uwp))


@api.route('/star/<code>/orbit/<int:orbit_no>/planet/<uwp>/albedo')
def get_albedo_star(code, orbit_no, uwp):
    '''Get albedo via star route'''
    del code
    del orbit_no
    return get_albedo(uwp)


@api.route('/planet/<uwp>/albedo')
def get_albedo(uwp):
    '''Process clouduness request'''
    planet = Planet(uwp)
    if planet.uwp:
        return jsonify({'albedo': planet.albedo})
    else:
        return errors.bad_request('Invalid UWP {}'.format(uwp))


@api.route('/star/<code>/orbit/<int:orbit_no>/planet/<uwp>/temperature')
def get_base_temperature(uwp, code, orbit_no):
    '''Process clouduness request'''
    star = Star(code)
    orbit = Orbit(star, orbit_no)
    planet = Planet(uwp, star=star, orbit=orbit)
    if planet.uwp:
        return jsonify({'temperature': planet.temperature})
    else:
        return errors.bad_request('Invalid UWP {}'.format(uwp))
