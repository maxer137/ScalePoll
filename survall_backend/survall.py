from objects.answer import Answer
from objects.question import Question

from objects.user_question import UserQuestionPair
from objects.authentication import Authentication
from database.sql_database import SQLDatabase
from openai_class import OpenAiClass

class Survall():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Survall, cls).__new__(cls)
        return cls.instance
    
    def setup(self, openai, inject_mock_data):
        self.database = SQLDatabase(inject_mock_data=inject_mock_data)
        self.openai = OpenAiClass(openai)

        self.question_iteration = 0

    def register_authentication(self, authentication:Authentication):
        self.database.register_authentication(authentication)

    def get_previous_questions(self, authentication:Authentication):
        return self.database.get_previous_questions(authentication)
        
    def authenticate(self, session_token):
        return self.database.check_authentication(session_token)

    def get_question(self) -> Question:
        # Get a question a specific user UUID hasn't answered yet
        # If relevant generate a new question
        self.question_iteration += 1
        return self.database.get_iterated_question(self.question_iteration)
    
    def get_question_by_id(self, answer:Answer):
        return self.database.get_question_by_uuid(question_uuid=answer.question_uuid)
    
    def save_answer(self, answer:Answer, user_question_pair:UserQuestionPair):
        if not self.database.check_if_user_answered_question(user_question_pair=user_question_pair):
            self.database.save_answer(answer=answer, user_question_pair=user_question_pair)

        # TODO return question statistics

    def generate_new_question(self, question:Question):
        # If a question has been answered enough times and has enough relevance, a follow up question is generated and added to the database
        if(question.answers_count * question.relevance_sum >= 30):
            follow_up_question, question_explanation = Survall().openai.follow_up_question_query(question,Survall().database.get_answers_of_question(question))
            new_question = Question(follow_up_question, question_explanation,question.uuid,question.root_question_uuid)
            Survall().save_question(question=new_question)

    def save_question(self, question:Question):
        self.database.save_question(question=question)
