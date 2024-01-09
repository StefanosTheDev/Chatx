from flask import Flask
from DB.db import db
from API.UserAPI import userAPI
# Make sure to import your models here

app = Flask(__name__, static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_super_secret_key'

db.init_app(app)

app.register_blueprint(userAPI)

with app.app_context():
    # Import models here, if they are not already
    db.create_all()

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)
