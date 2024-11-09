from flask_restful import Resource, reqparse
from flask import request
from uuid import uuid4


class Login(Resource):
    def post(self):
        # TODO: Ronald! Use your magic to get this hash into a temporary database with the rand token.
        print(request.get_json()['hash'])
        rand_token = str(uuid4())
        return rand_token, 200

