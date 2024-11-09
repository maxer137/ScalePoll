import uuid

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.sql_base import Base

class Question(Base):
    __tablename__ = 'questions'  # Table name in the database

    uuid = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    
    parent_question_uuid = Column(String, ForeignKey('questions.uuid'), nullable=True)  # Nullable for root-level questions
    root_question_uuid = Column(String, ForeignKey('questions.uuid'), nullable=True)

    # Relationships to allow navigation of the hierarchy
    parent_question = relationship(
        "Question", 
        remote_side=[uuid],
        foreign_keys=[parent_question_uuid],
        backref="child_questions")
    root_question = relationship(
        "Question", 
        remote_side=[uuid],
        foreign_keys=[root_question_uuid],
        backref="family_questions")

    question = Column(String)
    description = Column(String)

    amount_positive = Column(Integer)
    amount_neutral = Column(Integer)
    amount_negative = Column(Integer)
    relevance_sum = Column(Integer)
    answers_count = Column(Integer)
    discussion_count = Column(Integer)

    def __init__(self, question, description, parent_question_uuid=None, root_question_uuid=None):
        self.uuid = str(uuid.uuid4())

        self.question = question
        self.description = description

        self.parent_question_uuid = parent_question_uuid
        self.root_question_uuid = root_question_uuid

        self.amount_positive = 0
        self.amount_neutral = 0
        self.amount_negative = 0
        self.relevance_sum = 0
        self.answers_count = 0
        self.discussion_count = 0

    def get_uuid(self):
        return str(self.uuid)

    def to_dict(self):
        return {
            "uuid": self.uuid,
            "question": self.question,
            "description": self.description,
            "positive":self.amount_positive,
            "neutral":self.amount_neutral,
            "negative":self.amount_negative,
            "relevance_sum":self.relevance_sum,
            "answers_count":self.answers_count,
            "discussion_count":self.discussion_count
        }

    def to_json(self):
        return self.to_dict()


    def calculate_threshold(self):
        return self.discussion_count * (self.relevance_sum/self.answers_count)
    
    def __str__(self):
        # Custom string representation
        return (
            f"Question(uuid={self.uuid}, "
            f"question={self.question}, "
            f"description={self.description}, "
            f"positive={self.amount_positive}, "
            f"neutral={self.amount_neutral}, "
            f"negative={self.amount_negative}, "
            f"relevance_sum={self.relevance_sum}, "
            f"answers_count={self.answers_count}, "
            f"discussion_count={self.discussion_count})"
        )