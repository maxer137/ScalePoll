from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from openai import OpenAI
from dotenv import load_dotenv

from endpoints.questions_endpoint import RequestQuestion

from survall import Survall

# Load environment variables
load_dotenv()

# Initialize OpenAI
openai = OpenAI()

Survall().setup(openai)

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

api.add_resource(RequestQuestion, '/get_question')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=1337)


        