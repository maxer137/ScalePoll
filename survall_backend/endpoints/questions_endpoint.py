import json
from flask_restful import Resource
from flask import request

from survall import Survall
from objects.question import Question
from objects.answer import Answer
from objects.user_question import UserQuestionPair
from objects.authentication import Authentication

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

        print(answer.to_json())

        return 200
    
class PreviousQuestions(Resource):
    def get(self):
        authentication:Authentication = Survall().authenticate(request.headers.get('Authorization'))
        if authentication is None: return 401

        print(authentication.user_hash)

        previous_questions = Survall().get_previous_questions(authentication)

        previous_questions_dict_list = [question.to_dict() for question in previous_questions]
        questions_json = json.dumps(previous_questions_dict_list)

        return previous_questions_dict_list, 200