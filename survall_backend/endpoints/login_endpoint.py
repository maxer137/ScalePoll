from flask_restful import Resource, reqparse
from flask import request
from uuid import uuid4

from objects.authentication import Authentication
from survall import Survall


class Login(Resource):
    def post(self):
        authentication:Authentication = Authentication(user_hash=request.get_json()['hash'])

        Survall().register_authentication(authentication)

        return authentication.to_json(), 200

class ExampleAuthenticate(Resource):
    def post(self):
        authentication:Authentication = Survall().authenticate(request.headers.get('Authorization'))
        if authentication is None: return 401
        
        # Do other stuff with the user_hash afterwards
        print(authentication.user_hash)

        return authentication.to_json(), 200