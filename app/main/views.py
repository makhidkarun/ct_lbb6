'''views'''

from flask import render_template, redirect, url_for, abort, request,\
    current_app, make_response
from . import main
from .. import db
