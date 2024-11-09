import os
import uuid
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from objects.answer import Answer
from objects.user_question import UserQuestionPair

from objects.question import Question
from database.sql_base import Base

class SQLDatabase():
    def __init__(self, DATABASE_NAME='survall.db', inject_mock_data=True):
        # Setup the SQLite engine
        self.db_url = f'sqlite:///{DATABASE_NAME}'
        self.engine = create_engine(self.db_url, echo=True)

        # Create all the tables (Question, Answer, UserQuestionAnswer)
        Base.metadata.create_all(self.engine)

        # Create a session to interact with the database
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        if inject_mock_data:
            self.inject_mock_data() 

    def get_random_question(self):
        return self.session.query(Question).order_by(func.random()).first()
    
    def check_if_user_answered_question(self, user_question_pair:UserQuestionPair):
        existing_answer = self.session.query(UserQuestionPair).filter_by(
            user_uuid=user_question_pair.user_uuid, 
            question_uuid=user_question_pair.question_uuid).first()

        if not existing_answer:
            return False
        return True
    
    def save_question(self, question:Question):
        # TODO check if the question not already exists

        self.session.add(question)
        self.session.commit()
    
    def save_answer(self, answer:Answer, user_question_pair:UserQuestionPair):
        # TODO update question statistics

        self.session.add(answer)
        self.session.add(user_question_pair)
        self.session.commit()

    def get_answers_of_question(self, question):
        return self.session.query(Answer).filter(Answer.question_uuid == question.uuid).all()

    # Example of querying the database
    def get_answer_by_uuid(self, answer_uuid):
        return self.session.query(Answer).filter(Answer.uuid == answer_uuid).first()
    
    def inject_mock_data(self):
        mock_question = Question("This is a mock question, right?", "This is its description.") # This is a root question so no parent or root uuid is set
        mock_answer = Answer(
            question_uuid=mock_question.get_uuid(),
            answer_score=1, # Options: -1,0,1
            relevance_score=3, # Range: 1-5
            discussion="I think the discussion should be more about what questions are."
            )
        mock_question.amount_positive +=1 # As Answerscore is 1 (postive)
        mock_question.answers_count +=1
        mock_question.relevance_sum += mock_answer.relevance_score

        mock_user_question_pair = UserQuestionPair(
            user_uuid=str(uuid.uuid4()),
            question_uuid=mock_question.get_uuid()
        )

        self.save_question(question=mock_question)
        self.save_answer(answer=mock_answer, user_question_pair=mock_user_question_pair)

        print(mock_question.to_json())
        print(mock_answer.to_json())

    def reset_database(self):
        """Drops and recreates all tables"""

        self.session.close()

        print("Resetting the database...")
        if os.path.exists(self.db_url.split(':///')[1]):  # Check if the database file exists
            os.remove(self.db_url.split(':///')[1])  # Remove the old database file

        # Drop all existing tables
        Base.metadata.drop_all(self.engine)

        # Recreate tables
        Base.metadata.create_all(self.engine)
        print("Database reset complete.")

        
        
   











