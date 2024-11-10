from flask_restful import Resource
from flask import request
import hmac
import hashlib
import requests
import os

class Login(Resource):
    def post(self):
        # Example usage:
        secret_key = os.getenv('SURVALL_SECRET_KEY')  # Keep this key secure!
        user = request.get_json()
        user = str(user['user'])
        if user is None:
            return "not a valid login", 400
        if not user.isnumeric():
            return "not a valid login", 400
        number = int(user)  # User's login number
        anonymous_id = generate_anonymous_id(number, secret_key)
        return get_cookie(anonymous_id), 200


def generate_anonymous_id(number, secret_key):
    # Use HMAC with a secret key to hash the number
    h = hmac.new(secret_key.encode(), str(number).encode(), hashlib.sha256)
    # Return the hex digest as the anonymous identifier
    return h.hexdigest()

def get_cookie(hash_input):
    response = requests.post('http://127.0.0.1:1337/login', json={'hash': hash_input})
    return response.json()
    # return hash