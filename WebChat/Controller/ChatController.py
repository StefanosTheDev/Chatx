import logging
from flask import jsonify, Blueprint, request, render_template

chat_blueprint = Blueprint('chat', __name__)

profiles = [
    {"name": "User 1", "email": "user1@example.com"},
    {"name": "User 2", "email": "user2@example.com"},
    {"name": "User 3", "email": "user3@example.com"},
        {"name": "User 1", "email": "user1@example.com"},
    {"name": "User 2", "email": "user2@example.com"},
    {"name": "User 3", "email": "user3@example.com"},
        {"name": "User 1", "email": "user1@example.com"},
    {"name": "User 2", "email": "user2@example.com"},
    {"name": "User 3", "email": "user3@example.com"},
        {"name": "User 1", "email": "user1@example.com"},
    {"name": "User 2", "email": "user2@example.com"},
    {"name": "User 3", "email": "user3@example.com"},
        {"name": "User 1", "email": "user1@example.com"},
    {"name": "User 2", "email": "user2@example.com"},
    {"name": "User 3", "email": "user3@example.com"},

    {"name": "User 3", "email": "user3@example.com"},
        {"name": "User 1", "email": "user1@example.com"},
    {"name": "User 2", "email": "user2@example.com"},
    {"name": "User 3", "email": "user3@example.com"},
        {"name": "User 1", "email": "user1@example.com"},
    {"name": "User 2", "email": "user2@example.com"},
    {"name": "User 3", "email": "user3@example.com"}
    # Add more profiles as needed
]
@chat_blueprint.route('/chat', methods=['GET'])
def chat_homepage():
    return render_template('chat.html', profiles=profiles)
