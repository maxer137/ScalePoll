from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from openai import OpenAI
from dotenv import load_dotenv

from survall import Survall
from endpoints.openai_endpoint import RequestOpenAi
from endpoints.questions_endpoint import AnswerQuestion, RequestQuestion
from endpoints.login_endpoint import ExampleAuthenticate, Login

# Load environment variables
load_dotenv()

# Initialize OpenAI
openai = OpenAI()


inject_mock_data = True
Survall().setup(openai, inject_mock_data)

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

# @app.errorhandler(Exception)
# def handle_exception(e):
#     print(e)

#     # You could log the error here, if desired
#     response = {
#         "message": "An internal error occurred. Please try again later."
#     }
#     return response, 500

api.add_resource(RequestQuestion, '/get_question')
api.add_resource(AnswerQuestion, '/post_answer')
api.add_resource(RequestOpenAi, '/get_openai')
api.add_resource(Login, '/login')
api.add_resource(ExampleAuthenticate, '/authentication_example')


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=1337)
      