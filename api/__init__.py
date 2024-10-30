from flask import (
  Flask, request, jsonify
)
from flask_cors import CORS
from flask_session import Session
from config import Config
from api.extensions import db
from dotenv import load_dotenv
from api.models.article import Article
from api.models.user import User
from werkzeug.security import (
  generate_password_hash, check_password_hash
)
from redis import Redis

load_dotenv()
def create_app(config_object=Config):
  app = Flask(__name__)
  app.config.from_object(config_object)
  # enable CORS
  CORS(app)

  # Enable server-side sessions
  Session(app)

  # Initailize database
  db.init_app(app)
  app.config['SESSION_REDIS'] = Redis(host='localhost', port=6379)
  with app.app_context():
    # db.drop_all()
    db.create_all()


  @app.route('/')
  def index():
    return 'hello world'

  @app.route('/like', methods=['POST'])
  def like_post():
    data = request.get_json()
    article = Article.query.filter(Article.id == data['articleID']).first()

    if article:
      article.like_count += 1

      return jsonify({'message': 'Liked post'})

    return jsonify({'message': 'Not authorized'}), 403


  @app.route('/register', methods=['POST'])
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
      return jsonify({'message': 'An error occured while creating user', 'error': str(e)}), 500


  @app.route('/login', methods=['POST'])
  def login():
    data = request.get_json()
    # check if email and password are empty
    if data['email'] and data['password']:
      user = User.query.filter(User.email)
    

  return app
