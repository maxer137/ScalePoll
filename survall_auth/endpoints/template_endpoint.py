from flask_restful import Resource, reqparse
from flask import request
import hmac
import hashlib
import requests
import os


class TemplateEndpoint(Resource):
    def get(self):
        return "Test", 418

class Login(Resource):
    def post(self):
        # Example usage:
        secret_key = os.getenv('SURVALL_SECRET_KEY')  # Keep this key secure!
        print(request.get_json())
        user = '0'
        if user is None:
            return "not a valid login", 400
        if not user.isnumeric():
            return "not a valid login", 400
        number = int(user)  # User's login number
        print(number)
        anonymous_id = generate_anonymous_id(number, secret_key)
        return get_cookie(anonymous_id), 200


def generate_anonymous_id(number, secret_key):
    # Use HMAC with a secret key to hash the number
    h = hmac.new(secret_key.encode(), str(number).encode(), hashlib.sha256)
    # Return the hex digest as the anonymous identifier
    return h.hexdigest()

def get_cookie(hash):
    # response = requests.get('http://127.0.0.1:1337/login?hash=' + hash)
    # return response.content
    return hash