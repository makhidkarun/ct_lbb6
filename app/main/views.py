'''views'''

from flask import render_template, current_app
from . import main
from .forms import Lbb6Form
from .star import Star
from .orbit import Orbit
from .planet import Planet


@main.route('/', methods=['GET', 'POST'])
def index():
    '''Index page'''
    star = Star('')
    orbit = Orbit(star, None)
    planet = Planet(None, orbit, star)
    form = Lbb6Form()
    current_app.logger.debug('star data = %s', form.star.data)
    current_app.logger.debug('orbit data = %s', form.orbit.data)
    current_app.logger.debug('planet data = %s', form.planet.data)
    if form.validate_on_submit():
        current_app.logger.debug('form validated')
        star = Star(form.star.data)
        if form.orbit.data is not None:
            orbit = Orbit(star, form.orbit.data)
        if form.planet.data:
            planet = Planet(form.planet.data, orbit=orbit, star=star)
        current_app.logger.debug(
            'star.classification = %s', star.classification)
        current_app.logger.debug('orbit.orbit_no = %s', orbit.orbit_no)
        current_app.logger.debug('planet.uwp = %s', planet.uwp)
    return render_template(
        'index.html',
        star=star,
        orbit=orbit,
        planet=planet,
        form=form)
