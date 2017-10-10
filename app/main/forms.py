'''forms.py'''

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required, Optional, Regexp

UWP_REGEXP = r'^[A-HYX][0-9A-HJ-NP-Z]{6}\-[0-9A-HJ-NP-Z]$'
STAR_REGEXP = r'([BAFGKM])([0-9])\s*([IVDab]{1,2}$)|[BAFGKM]\s*D$'


class Lbb6Form(FlaskForm):
    '''Form for star/orbit/planet'''
    star = StringField(
        'Star code',
        validators=[Required(), Regexp(STAR_REGEXP)])
    orbit = IntegerField('Orbit number', validators=[Optional()])
    planet = StringField(
        'Planet UWP',
        validators=[Optional(), Regexp(UWP_REGEXP)])
    submit = SubmitField('Submit')
