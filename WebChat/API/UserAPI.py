import logging
from flask import jsonify, Blueprint, request
from Service.UserService import UserService

userAPI = Blueprint('userapi', __name__)

@userAPI.route('/userapi/create_account', methods=['POST'])
def create_account():
    try:
        data = request.get_json() # Assuming data is sent as JSON
        new_account = UserService.create_account(
            username=data['username'],
            password=data['password'],
            email = data['email']
        )
        return jsonify({'Accounts': f"{new_account}"}), 201
    except Exception as e:
         return jsonify({'error': f'{str(e)}'}), 500

@userAPI.route('/userapi/getAccounts',methods=['GET'])
def getAccounts():
    try:
        all_accounts = UserService.get_accounts()
        if not all_accounts:
            return jsonify({'message': 'No Accounts Found'}), 404
        return jsonify({'Accounts fetched': all_accounts}), 201
    except Exception as e:
         return jsonify({'error': f'{str(e)}'}), 500


@userAPI.route('/userapi/login', methods=['POST'])
def login():
    try:
        data = request.get_json() # Data sent as json
        account = UserService.login(
        username=data['username'],
        password=data['password']
        )
        return jsonify({'Account': f"{account}"})
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
            return jsonify({'message': 'Account deleted successfully'}), 200
        else:
         return jsonify({'error': 'Account not found'}), 404
    except Exception as e:
        return jsonify({'error': e})

