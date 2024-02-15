from Models.User import UserModel
from DB.db import db
from GlobalExceptions.ServiceExecption import ServiceException, UsernameError, PasswordError
from flask import session
from sqlalchemy.exc import IntegrityError, OperationalError
import bcrypt

class UserService:

    #** TODO Upon Registering the account, Encrypt the Password.
    #** 


    def create_account(username, password, email):
        try:
        # Hash the password
            UserService.check_username(username) # Check the Username
            UserService.check_password(password) # Check the Password
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Create the user account with the hashed password
            create_acc = UserModel(username=username, password=hashed_password, email=email)
            db.session.add(create_acc)
            db.session.commit()
        
            return create_acc
        except Exception as e:
            db.session.rollback()
            raise

    def login(username, password):
        try:
            # Search the DB fo rth euser.
            user = UserModel.query.filter_by(username=username).first()
            if not user:
                raise UsernameError("User does not exist")
            
        # Check if the hashed password matches the entered password
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            # Set user logged-in session
                session['logged_in'] = True
                session['user_id'] = user.id
                session['username'] = user.username
                return user
            else:
                raise PasswordError("Incorrect password")
        except (UsernameError, PasswordError) as e:
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



    

#*TODO check if i need logout like this
    def logout():
        return session.clear()
    
    def update_account(id, updatedUsername, updatedPass):
        try:
            user = UserService.return_account_by_Id(id)
            if updatedUsername != user.username:
                user.username = updatedUsername
            if updatedPass:
                user.password = updatedPass  # ideally, you should hash the password before storing it
            db.session.commit()

            return user
        
        except ServiceException as e:  # catch the custom exception
            db.session.rollback()
            raise
        
        except Exception as e:  # catch all other exceptions
            db.session.rollback()
            raise
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
        
    def delete_account_by_Id(id):
        try: 
            user_account = UserService.return_account_by_Id(id)
            if user_account:
                db.session.delete(user_account)
                db.session.commit()
                return user_account
        except ServiceException as e:
            db.session.rollback()
            raise
        except Exception as e:
            db.session.rollback()
            raise
    def add_friend_to_user(self, user_id, friend_username):
        try:
            user = UserService.return_account_by_Id(user_id)
        except Exception as e:
            pass

    def searchByUsername(username):
        pass

    def check_username(username):
        if len(username) <= 5 or len(username) > 12:
            raise UsernameError("Error with length of username") 

        has_upper = any(letter.isupper() for letter in username)
        has_lower = any(letter.islower() for letter in username)
        if not(has_upper and has_lower):
            raise UsernameError("Username does not have an upper and lower case letter")
        return True
    
    def check_password(password):
        SPECIAL_CHARACTERS = "!@#$%^&*"
        if len(password) <= 5 or len(password) > 16:
            raise PasswordError('Password does not meet length requirements')

        has_upper = any(letter.isupper() for letter in password)
        has_lower = any(letter.islower() for letter in password)
        if not (has_upper and has_lower):
            raise PasswordError("Password does not meet capitalization requirements")
        if not any(char.isdigit() for char in password):
            raise PasswordError("Password does not contain a numeric value")
        if not any(char in SPECIAL_CHARACTERS for char in password):
            raise PasswordError("Password does not contain a special character")
    
        return True
      