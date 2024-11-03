from flask import (
  request, jsonify, session
)
from api.models.user import User
from api.extensions import db

from api.routes.auth import bp
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import exc

@bp.route('/register', methods=['POST'])
def register():
  data = request.get_json()
  user = User.query.filter(User.username == data['username'] or User.email == data['email']).first()
  # check if a user with same userame or email already exists
  if user:
    return jsonify({'message': 'User already exists'}), 409

  try:
    # create a new user
    new_user = User(email=data['email'], password_hash=generate_password_hash(data['password']), username=data['username'])

    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201
  except Exception as e:
    db.session.rollback()
    # if e is exc.IntegrityError:
    return jsonify({'message': 'An error occured while creating user', 'error': str(e)}), 500


@bp.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  # check if email and password are empty
  try:
    if data['email'] and data['password']:
      user = User.query.filter(User.email == data['email']).first()
      if user:
        # check if password is correct
        if check_password_hash(user.password_hash, data['password']):
          session['user_id'] = user.id
          
          return jsonify({'message': "You've loged in successfully"}), 200
        else:
          return jsonify({'message': 'Wrong password'}), 401
      
      return jsonify({'message': 'User does not exist'}), 404
    return jsonify({'message': 'Email and password are required'}), 400
  except Exception as e:
    return jsonify({'message': 'There was an error logging in', 'error': str(e)}), 500

