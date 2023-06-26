from flask import Blueprint


user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/', methods=['GET'])
def get_all_users():
    pass


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_exact_user(user_id: int):
    pass


@user_bp.route('/<int:user_id>', methods=['PUT'])
def change_user_info(user_id: int):
    pass


@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_exact_user(user_id: int):
    pass
