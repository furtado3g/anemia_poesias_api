from flask import Flask, request, jsonify, make_response
from src.controllers.User import UserController
from datetime import datetime

app = Flask(__name__)


@app.route('/api/user', methods=['POST'])
def create_user():
    user_object = request.get_json()
    user = UserController().create(
        name=user_object['name'],
        email=user_object['email'],
        username=user_object['username'],
        password=user_object['password'],
        joindate=datetime.now(),
        birthday=datetime.strptime(user_object['birthday'],'%d/%m/%Y'),
        perfil_image=user_object['perfil_image'],
    )
    response = jsonify(user_object)
    response.status_code = 201
    response.content_type = 'application/json'
    return response

@app.route('/api/session', methods=['POST'])
def login():
    login_info = request.get_json()
    user = UserController().login(
        username=login_info['username'],
        password=login_info['password'],
    )
    return jsonify(user)