from flask import Blueprint


hastag_bp = Blueprint('hashtag', __name__, url_prefix='/hashtag')


@hastag_bp.route('/', methods=['GET'])
def get_hashtags(size: int):
    pass


@hastag_bp.route('/<string:hashtag_name>', methods=['GET'])
def get_exact_hashtag(hashtag_name: str):
    pass
