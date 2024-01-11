import logging
from flask import jsonify, Blueprint, request, render_template

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/', methods=['GET'])
def home():
    return render_template('index.html')
@home_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@home_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')