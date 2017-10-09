'''views'''

import logging
from flask import render_template
from . import main
from .forms import Lbb6Form
from .star import Star
from .orbit import Orbit
from .planet import Planet
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.ERROR)


@main.route('/', methods=['GET', 'POST'])
def index():
    '''Index page'''
    star = Star('')
    orbit = Orbit(star, None)
    planet = Planet(None, orbit, star)
    form = Lbb6Form()
    LOGGER.debug('star data = %s', form.star.data)
    LOGGER.debug('orbit data = %s', form.orbit.data)
    LOGGER.debug('planet data = %s', form.planet.data)
    if form.validate_on_submit:
        LOGGER.debug('form validated')
        star = Star(form.star.data)
        if form.orbit.data is not None:
            orbit = Orbit(star, form.orbit.data)
        if form.planet.data:
            planet = Planet(form.planet.data, orbit=orbit, star=star)
        LOGGER.debug('star.classification = %s', star.classification)
        LOGGER.debug('orbit.orbit_no = %s', orbit.orbit_no)
        LOGGER.debug('planet.uwp = %s', planet.uwp)
        return render_template(
            'index.html',
            star=star,
            orbit=orbit,
            planet=planet,
            form=form)
