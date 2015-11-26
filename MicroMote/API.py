from flask import Blueprint, render_template

PATH = '/api/v1/{}'

API = Blueprint('API', __name__)

@API.route(PATH.format('<device>/power'))
def toggle_power(device):
    # TODO: Send power button
    return "OK!"
