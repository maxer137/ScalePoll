from flask_restful import Resource
from flask import request

from survall import Survall
from objects.question import Question
from objects.answer import Answer
from objects.user_question import UserQuestionPair

class RequestQuestion(Resource):
    def get(self):
        question:Question = Survall().get_question()

        json_question = question.to_json()

        return json_question, 200
    
class AnswerQuestion(Resource):
    def post(self):
        data = request.get_json()

        answer:Answer = Answer.from_dict(data)
        user_question_pair:UserQuestionPair = UserQuestionPair.from_dict(data)

        Survall().save_answer(answer, user_question_pair)

        Survall().generate_new_question()

        return 200