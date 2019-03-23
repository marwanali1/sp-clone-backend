from app import db
from app.auth import bp
from app.models import User
from flask import jsonify, request, make_response
from flask_login import current_user, login_user, logout_user


@bp.route('/login', methods=['GET'])
def login():
    # if current_user.is_authenticated:
    #     pass

    auth_dict = {
        'isLoggedOn': True
    }

    return make_response(jsonify(auth_dict))


@bp.route('/logout')
def logout():
    logout_user()


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        pass
    pass
