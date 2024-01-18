import json
from DB.db import db


class Friendship(db.Model):
    __tablename__= 'friendships'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100),  nullable=False)
    
    #friendships = db.relationship('Friendship', foreign_keys=[Friendship.user_id], back_populates='user')
   # friends = db.relationship('UserModel', secondary='friendships', primaryjoin=id == Friendship.user_id, secondaryjoin=id == Friendship.friend_id, back_populates='friendships')


    def __init__(self, username, password, email):
        self.username = username
        self.password = password  # Hash the password before storing
        self.email = email
        '''
    def add_friend(self, friend_user):
        if friend_user not in self.friends:
            self.friends.append(friend_user)

    def remove_friend(self, friend_user):
        if friend_user in self.friends:
            self.friends.remove(friend_user)
        '''
    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,

        }

    def __str__(self):
        return str(self.json())

    def __repr__(self):
        return self.__str__()
