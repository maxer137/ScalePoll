import uuid

from sqlalchemy import ForeignKey, Integer, Column, String
from sqlalchemy.orm import relationship

from database.sql_base import Base

class Answer(Base):
    __tablename__ = 'answers'
    
    # Fields for Answer class
    uuid = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))  # Primary Key for Answer
    question_uuid = Column(String, ForeignKey('questions.uuid'), nullable=False)  # Foreign Key to Question

    discussion = Column(String)
    answer_score = Column(Integer)
    relevance_score = Column(Integer)

    # Relationships
    question = relationship("Question", backref="answers")  # Relationship with the Question model
    
    # Fields that should not be saved to the DB
    answer_score = None
    relevance_score = None

    def __init__(self, question_uuid, answer_score, relevance_score, discussion):
        self.uuid = str(uuid.uuid4())

        self.question_uuid = question_uuid
        self.answer_score = answer_score  # Not saved in the DB
        self.relevance_score = relevance_score  # Not saved in the DB
        self.discussion = discussion

    def to_dict(self):
        return {
            "question_uuid": self.question_uuid,
            "answer_score": self.answer_score,
            "relevance_score": self.relevance_score,
            "discussion": self.discussion,
        }

    def to_json(self):
        return self.to_dict()
    
    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            question_uuid=data["question_uuid"],
            answer_score=data["answer_score"],
            relevance_score=data["relevance_score"],
            discussion=data["discussion"]
        )