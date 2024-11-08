from flask_restful import Resource
from flask import jsonify

from survall import Survall
from objects.question import Question

class RequestOpenAi(Resource):
    def get(self):
        question:Question = Survall().question_list.get_question()

        json_question = question.to_json()

        return json_question, 200