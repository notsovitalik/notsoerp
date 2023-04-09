from flask import Blueprint
from flask import render_template, request
from flask_login import login_required

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
@login_required
def home():
    return render_template('modules/modules.html', title = 'about')

@main.route('/about')
def about():
    return render_template('about/about.html', title = 'about')

@main.route('/modules')
def modules():
    return render_template('modules/modules.html', title = 'modules')


