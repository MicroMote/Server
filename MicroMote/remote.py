from flask import Blueprint, render_template

remote = Blueprint('remote', __name__)

@remote.route('/')
def index():
    # TODO: Make a page
    return "OK!"
