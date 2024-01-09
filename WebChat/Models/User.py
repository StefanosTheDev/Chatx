from DB.db import db
class UserModel():
    __table__ = 'users'

    ## define the user column
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    friends = db.Column(db.ARRAY(db.String()))
    messages = db.Column(db.ARRAY(db.String(300), nullable=True))

    def __init__(self, username, password, friends=None, messages=None):
        self.username = username, 
        self.password = password,
        self.friends = friends,
        self.messages = messages
    
    def __str__(self):
        return(self.json)
    
    def __repr__(self):
        return self.__str__()
    
    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'friends': self.friends,
            'messages': self.messages
        }