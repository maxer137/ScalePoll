from objects.answer import Answer
from objects.question import Question

from objects.user_question import UserQuestionPair
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

    def get_question(self) -> Question:
        # Get a question a specific user UUID hasn't answered yet
        # If relevant generate a new question

        # TODO require UUID

        return self.database.get_random_question()
    
    def save_answer(self, answer:Answer, user_question_pair:UserQuestionPair):
        if not self.database.check_if_user_answered_question(user_question_pair=user_question_pair):
            self.database.save_answer(answer=answer, user_question_pair=user_question_pair)

        # TODO return question statistics

    def save_question(self, question:Question):
        self.database.save_question(question=question)
