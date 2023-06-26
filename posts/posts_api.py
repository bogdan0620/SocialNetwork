from flask import Blueprint

post_bp = Blueprint('user_post', __name__, url_prefix='/post')


@post_bp.route('/', methods=['GET'])
def get_all_user_posts():
    pass


@post_bp.route('/<int:post_id>', methods=['GET'])
def get_user_post(post_id: int):
    pass

@post_bp.route('/<int:user_id>/<int:post_id>', methods=['PUT'])
def change_user_post(user_id: int, post_id: int):
    pass


@post_bp.route('/<int:user_id>/<int:post_id>', methods=['DELETE'])
def delete_user_post(user_id: int, post_id: int):
    pass


@post_bp.route('/upload_post', methods=['POST'])
def create_post(post_text: str, post_photo: str, hashtags: list, user_id: int):
    pass
