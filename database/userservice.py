from models import User, Password, db


def register_user_db(**user_data):
    new_user = User(**user_data)

    db.session.add(new_user)
    db.session.commit()


def check_user_db(email):
    pass


def check_user_password_db(email, password):
    pass


def get_all_users_db():
    pass


def get_exact_user_db(user_id):
    pass


def delete_user_db(user_id):
    pass
