from flask import (
  Flask, request, jsonify
)
from flask_cors import CORS
from config import Config
from api.extensions import db
from dotenv import load_dotenv
from api.models.article import Article

load_dotenv()
def create_app(config_object=Config):
  app = Flask(__name__)
  app.config.from_object(config_object)
  # enable CORS
  CORS(app)

  # Initailize database
  db.init_app(app)

  with app.app_context():
    db.drop_all()
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

    

  return app
