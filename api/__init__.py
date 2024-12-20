from flask import (
  Flask, request, jsonify, session
)
from flask_cors import CORS
from flask_session import Session
from config import Config
from api.extensions import db
from dotenv import load_dotenv
from api.models.article import Article
from api.models.user import User

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

  with app.app_context():
    db.drop_all()
    db.create_all()

  
  from api.routes.main import bp as main_bp
  app.register_blueprint(main_bp)

  from api.routes.auth import bp as auth_bp
  app.register_blueprint(auth_bp)



  return app


app = create_app()
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
