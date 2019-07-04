from app import db
from app.auth import bp
from app.models import User
from flask import jsonify, request, make_response


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
    pass


@bp.route('/register', methods=['GET', 'POST'])
def register():
    pass
