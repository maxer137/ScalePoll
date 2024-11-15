from flask_restful import Resource

from survall import Survall
from objects.question import Question

# This is a mock implementation to generate a follow up question via the ChatGPT api
class RequestOpenAi(Resource):
    def get(self):
        question:Question = Survall().get_question()
        
        follow_up_question, question_explanation = Survall().openai.follow_up_question_query(question,Survall().database.get_answers_of_question(question))

        new_question = Question(follow_up_question, question_explanation)
        Survall().save_question(question=new_question)

        return follow_up_question, 200