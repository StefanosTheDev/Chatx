import json
from DB.db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    friends_list = db.Column(db.String(500))  # Assuming friends list will be stored as JSON string
    

    def __init__(self, username, password, email, friends_list=None):
        self.username = username
        self.password = password  # Hash the password before storing
        self.email = email
        self.friends_list = json.dumps(friends_list) if friends_list else None

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'friends_list': json.loads(self.friends_list) if self.friends_list else None
        }

    def __str__(self):
        return str(self.json())

    def __repr__(self):
        return self.__str__()
