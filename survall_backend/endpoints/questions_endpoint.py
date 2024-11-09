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

        json_question = question.to_dict_short()

        return json_question, 200
    
class AnswerQuestion(Resource):
    def post(self):
        data = request.get_json()

        authentication:Authentication = Survall().authenticate(request.headers.get('Authorization'))
        if authentication is None: return 401

        data['user_uuid'] = authentication.user_hash
        answer:Answer = Answer.from_dict(data)
        user_question_pair:UserQuestionPair = UserQuestionPair.from_dict(data)

        Survall().save_answer(answer, user_question_pair)

        related_question = Survall().get_question_by_id(answer)
        Survall().generate_new_question(related_question)

        print(related_question)

        return related_question, 200
    
class PreviousQuestions(Resource):
    def get(self):
        authentication:Authentication = Survall().authenticate(request.headers.get('Authorization'))
        if authentication is None: return 401

        print(authentication.user_hash)

        previous_questions = Survall().get_previous_questions(authentication)

        previous_questions_dict_list = [question.to_dict() for question in previous_questions]

        return previous_questions_dict_list, 200
    
class RelatedQuestions(Resource):
    def post(self):
        authentication:Authentication = Survall().authenticate(request.headers.get('Authorization'))
        if authentication is None: return 401

        print(authentication.user_hash)

        data = request.get_json()
        question:Question = Question.from_dict(data)

        related_questions = Survall().get_related_questions(question)
        related_questions_dict_list = [question.to_dict() for question in related_questions]

        return related_questions_dict_list, 200