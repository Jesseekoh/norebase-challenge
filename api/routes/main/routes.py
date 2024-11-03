from flask import (
  request, jsonify, session
)
from api.extensions import db
from flask_cors import cross_origin
from api.models.article import Article
from api.models.user import User
from api.routes.main import bp

@bp.route('/post/new', methods=['POST'])
def create_post():
  if session['user_id']:
    user_id = session['user_id']
    data = request.get_json()

    try:
      user = User.query.get(user_id)
      if user:
        new_article = Article(title=data['title'], content=data['content'])
        db.session.add(new_article)
        db.session.commit()
        return jsonify({'message': 'Article created successfully', 'data': {
          'article_id': str(new_article.id)
        }}), 201
      return jsonify({'message': 'Not authorized'}), 403
    except Exception as e:
      db.session.rollback()
      return jsonify({'message': 'An error occured while creating user', 'error': str(e)}), 500

      



@bp.route('/like', methods=['POST'])
@cross_origin(supports_credentials=True)
def like_post():
  if session['user_id']:
    print(session['user_id'])
    user_id = session['user_id']
    data = request.get_json()
    article = Article.query.filter(Article.id == data['articleID']).first()

    if article:
      user = User.query.filter(User.id == user_id).first()
      if user:
        if user not in article.liked_by_users:
          article.like_count += 1
          article.liked_by_users.append(user)
          # user.liked_articles_count += 1
          db.session.commit()
          return jsonify({'message': 'Liked post'})
        else:
          return jsonify({'message': 'User already liked this article'}), 409
      else:
        return jsonify({'message': 'User not found'}), 404
    else:
      return jsonify({'message': 'Article not found'}), 404
  return jsonify({'message': 'Not authorized'}), 403
