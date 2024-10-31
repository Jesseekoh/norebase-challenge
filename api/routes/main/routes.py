from flask import (
  request, jsonify
)

from flask_cors import cross_origin
from api.models.article import Article
from api.routes.main import bp
@bp.route('/like', methods=['POST'])
@cross_origin(supports_credentials=True)
def like_post():
  data = request.get_json()
  article = Article.query.filter(Article.id == data['articleID']).first()

  if article:
    article.like_count += 1

    return jsonify({'message': 'Liked post'})

  return jsonify({'message': 'Not authorized'}), 403
