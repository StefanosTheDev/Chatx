from Models.User import UserModel
from DB.db import db
from GlobalExceptions.ServiceExecption import ServiceException, UsernameError, PasswordError
from flask import session
from sqlalchemy.exc import IntegrityError, OperationalError
class UserService:
    def create_account(username, password):
        try:
            create_acc = UserModel(username=username, password=password)
            db.session.add(create_acc)
            db.session.commit()
            return create_acc
        except Exception as e:
            db.session.rollback()
            raise
    def get_accounts():
        try:
            accounts = UserModel.query.all()
            if not accounts:
                raise Exception('No Users were found in the DB')
            accounts_json = [accounts.json() for accounts in accounts]
            return accounts_json
        except Exception as e:
            db.session.rollback()
            raise

#*TODO Check if ineed a session etc. 
    def login(username, password):
        try:
            ## Write up if the dictionary object meets a specific thing     
            user = UserModel.query.filter_by(username=username).first() # query for the user oject.
            if not user:
                raise UsernameError("User does not exist")
            elif user.password == password:
                print(f"There is a match between {user.password} and {password}")
            elif user.password != password:
                raise PasswordError( "Incorrect password")
        
        # Set user logged-in session
           # session['logged_in'] = True
           # session['user_id'] = user.id
           # session['username'] = user.username
            return user
        except (UsernameError, PasswordError) as e:
           # logging.error(e)
            raise

#*TODO check if i need logout like this
    def logout():
        return session.clear()
    
    def update_account(id, updatedUsername, updatedPass):
        try:
            user = UserService.return_account_by_Id(id)
            if updatedUsername and updatedUsername != user.username:
                user.username = updatedUsername
            if updatedPass:
                user.password = updatedPass  # ideally, you should hash the password before storing it
            db.session.commit()

            return user
        
        except ServiceException as e:  # catch the custom exception
            db.session.rollback()
            raise ({'Error': str(e)})
        
        except Exception as e:  # catch all other exceptions
            db.session.rollback()
            raise ({'Error': str(e)})
    def return_account_by_Id(id):
        try:
            user = UserModel.query.get(id)
            if not user:
                raise ServiceException(f"No user found with the id {id}")
            return user
        except IntegrityError as e:
            raise ServiceException(f"Error Message: {e}")
        except OperationalError as e:  # catch any SQLAlchemy related errors
            raise ServiceException(f"Database Error: {e}")