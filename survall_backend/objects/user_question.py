from sqlalchemy import ForeignKey, PrimaryKeyConstraint, Column, String
from sqlalchemy.orm import relationship

from database.sql_base import Base

class UserQuestionPair(Base):
    __tablename__ = 'user_question_answers'
    
    question_uuid = Column(String, ForeignKey('questions.uuid'), nullable=False)
    user_uuid = Column(String, nullable=False)
    
    # This ensures that each user can only have one answer for a specific question
    __table_args__ = (PrimaryKeyConstraint('user_uuid', 'question_uuid'),)

    # Relationships
    question = relationship("Question", backref="user_answers")
    
    def __init__(self, user_uuid, question_uuid):
        self.user_uuid = user_uuid
        self.question_uuid = question_uuid

    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            question_uuid=data["question_uuid"],
            user_uuid=data["user_uuid"]
        )