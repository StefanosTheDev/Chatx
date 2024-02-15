import logging
from flask import jsonify, Blueprint, request, render_template, redirect, url_for, flash
import requests
from Forms.AuthForms import RegForm, LoginForm
from API.UserAPI import userAPI
from GlobalExceptions.ServiceExecption import UsernameError, PasswordError, ServiceException
home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/', methods=['GET'])
def home():
    return render_template('index.html')
from flask import flash, redirect, render_template

@home_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()

    try: 
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            email = form.email.data
            
            data = {
                'username': username, 
                'password': password,
                'email': email
            }
            response = requests.post(
                'http://127.0.0.1:5000/userapi/create_account',
                headers={'Content-Type': 'application/json'},
                json=data
            )
            if response.status_code == 201: 
                return redirect(url_for('home.login'))
            else: 
                error_message = response.json().get('error')  # Get the error message from the API response
                if error_message:
                    flash(error_message)  # Flash the error message
                    return render_template('register.html', form=form, error_message=error_message)
                else:
                    flash("Failed to create user")
    except Exception as e:
        flash("An error occurred while processing your request.")  # Generic error message
    return render_template('register.html', form=form)


@home_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    try:
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            data = {
            'username': username,
            'password': password
            }
            response = requests.post(
            'http://127.0.0.1:5000/userapi/login', 
             headers={'Content-Type': 'application/json'},
            json=data)

            if response.status_code == 200:
                return redirect(url_for('chat.chat_homepage'))
            
    except Exception as e:
        flash('Error', 'danger')
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)
