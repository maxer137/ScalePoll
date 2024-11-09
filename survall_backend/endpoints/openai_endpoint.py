from flask_restful import Resource
from flask import jsonify

from survall import Survall
from objects.question import Question

class RequestOpenAi(Resource):
    def get(self):
        # This is a mock implementation to generate a follow up question
        question:Question = Survall().database.get_random_question()
        
        follow_up_question = Survall().openai.follow_up_question_query(question,Survall().database.get_answers_of_question(question))

        return follow_up_question, 200