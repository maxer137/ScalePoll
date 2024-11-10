from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from openai import OpenAI
from dotenv import load_dotenv

from survall import Survall
from endpoints.openai_endpoint import RequestOpenAi
from endpoints.questions_endpoint import AnswerQuestion, BrewCoffee, ClosedQuestions, PreviousQuestions, RequestQuestion
from endpoints.login_endpoint import Login

load_dotenv()

# Initialize OpenAI API
openai = OpenAI()

inject_mock_data = True
Survall().setup(openai, inject_mock_data)

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

api.add_resource(RequestQuestion, '/get_question')
api.add_resource(AnswerQuestion, '/post_answer')
api.add_resource(RequestOpenAi, '/get_openai')
api.add_resource(Login, '/login')
api.add_resource(PreviousQuestions, '/previous_questions')
api.add_resource(ClosedQuestions, '/closed_questions')
api.add_resource(BrewCoffee, '/brew_coffee')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=1337)
      