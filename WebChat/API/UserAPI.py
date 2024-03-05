import logging
from flask import jsonify, Blueprint, request
from Service.UserService import UserService
from GlobalExceptions.ServiceExecption import ServiceException, UsernameError, PasswordError, UsernameTakenError
from sqlalchemy.exc import IntegrityError

userAPI = Blueprint('userapi', __name__)

@userAPI.route('/userapi/create_account', methods=['POST'])
def create_account():
    try:
        data = request.get_json() # Assuming data is sent as JSON
        
        UserService.check_create_api_params_exist(data) # Validate params comming into API exist. 
        new_account = UserService.create_account(
            username=data['username'],
            password=data['password'],
            email = data['email']
        )
        return jsonify({'Accounts': f"{new_account}"}), 201
    except (UsernameError, PasswordError, UsernameTakenError, KeyError) as error:
         return jsonify({'error': f'{str(error)}'}), 500

@userAPI.route('/userapi/login', methods=['POST'])
def login():
    try:
        data = request.get_json() # Data sent as json
        account = UserService.login(
        username=data['username'],
        password=data['password']
        )
        return jsonify({'Account': f"{account}"})
    except (UsernameError, PasswordError, UsernameTakenError, AttributeError) as error:
         return jsonify({'error': f'{str(error)}'}), 500

@userAPI.route('/userapi/getAccounts',methods=['GET'])
def getAccounts():
    try:
        all_accounts = UserService.get_accounts()
        if not all_accounts:
            return jsonify({'message': 'No Accounts Found'}), 404
        return jsonify({'Accounts fetched': all_accounts}), 201
    except Exception as e:
         return jsonify({'error': f'{str(e)}'}), 500


@userAPI.route('/userapi/update', methods=['POST'])
def update_account():
    pass

@userAPI.route('/userapi/delete/<int:id>', methods=['POST'])
def delete_account(id):
    try:
        account = UserService.delete_account_by_Id(id)
        if account:
            return jsonify({'message': 'Account deleted successfully'}), 200
        else:
         return jsonify({'error': 'Account not found'}), 404
    except Exception as e:
        return jsonify({'error': e})

@userAPI.route('/userapi/getAccount/<int:id>', methods=['GET'])
def getAccount_by_Id(id):
    try:
        account = UserService.return_account_by_Id(id)
        if account:
            return jsonify({'message': f"{account}"}), 200
        else:
         return jsonify({'error': 'Account not found'}), 404
    except Exception as e:
        return jsonify({'error': e})
        
@userAPI.route('/userapi/friendRequest/<string:username>', methods=['POST'])
def send_friend_request(username):
    pass


@userAPI.route('/userapi/friend_request_deny/<string:username>', methods=['POST'])
def deny_friend_request(username):
    pass


@userAPI.route('/userapi/friend_request/accept/<string:username>', methods=['POST'])
def accept_friend_request(username):
    pass

@userAPI.route('/userapi/search_by_username/<string:username>', methods=['POST'])
def search_by_username(username):
    pass

@userAPI.route('/userapi/remove_friend/<string:username>', methods=['POST'])
def remove_friend_by_username(username):
    pass

@userAPI.route('/userapi/sent_friend_requests/<string:username>', methods=['GET'])
def sent_friend_requests(username):
    pass

@userAPI.route('/userapi/friendsList/<string:username>', methods=['GET'])
def retrieve_friends_list(username):
    pass
