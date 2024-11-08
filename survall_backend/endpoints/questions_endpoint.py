from flask_restful import Resource
from flask import request

from survall import Survall
from objects.question import Question
from objects.answer import Answer

class RequestQuestion(Resource):
    def get(self):
        question:Question = Survall().database.get_question()

        json_question = question.to_json()

        return json_question, 200
    
class AnswerQuestion(Resource):
    def post(self):
        data = request.get_json()

        answer:Answer = Answer.from_dict(data)

        Survall().database.add_question(Question(answer.discussion))

        print(answer.to_json())

        return 200