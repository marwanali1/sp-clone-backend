from app import db, api
from app.models import User
from flask_restful import Resource


class Login(Resource):

    def get(self):
        auth_dict = {
            'isLoggedOn': True
        }
        return auth_dict


class Logout(Resource):

    def get(self):
        auth_dict = {
            'isLoggedOn': False
        }
        return auth_dict


api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
