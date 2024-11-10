from flask_restful import Resource
from flask import request

from objects.authentication import Authentication
from survall import Survall


class Login(Resource):
    def post(self):
        authentication:Authentication = Authentication(user_hash=request.get_json()['hash'])

        Survall().register_authentication(authentication)

        return authentication.to_json(), 200