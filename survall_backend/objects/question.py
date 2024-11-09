from datetime import datetime, timedelta, timezone
import uuid

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
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
    threshold_sum = Column(Integer)

    creation_time = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    close_time = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc) + timedelta(days=7))
    closed = Column(Boolean, default=False, nullable=False)

    def __init__(self, question, description, parent_question_uuid=None, root_question_uuid=None, creation_time=None, close_time=None):
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
        self.threshold_sum = 0

        self.creation_time = creation_time or datetime.now(timezone.utc)
        self.close_time = close_time or self.creation_time + timedelta(days=7)

    def get_uuid(self):
        return str(self.uuid)
    
    def close(self):
        """Set the close time to the current timestamp."""
        self.close_time = datetime.now(timezone.utc)

    def get_creation_time(self):
        if self.creation_time is not None:
            return self.creation_time.isoformat()
        return None

    def get_close_time(self):
        if self.close_time is not None:
            return self.close_time.isoformat()
        return None    

    def to_dict(self):
        return {
            "uuid":self.uuid,
            "question":self.question,
            "description":self.description,
            "positive":self.amount_positive,
            "neutral":self.amount_neutral,
            "negative":self.amount_negative,
            "relevance_sum":self.relevance_sum,
            "answers_count":self.answers_count,
            "discussion_count":self.discussion_count,
            "creation_time":self.get_creation_time(),
            "close_time":self.get_close_time(),
            "closed":self.closed
        }
    
    def to_dict_short(self):
        return {
            "uuid":self.uuid,
            "question":self.question,
            "description":self.description,
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
            f"discussion_count={self.discussion_count}), "
            f"creation_time={self.get_creation_time()}, "
            f"close_time={self.get_close_time()})"
            f"closed={self.closed}"
        )
    
    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            question_uuid=data["question_uuid"],
            question = data["question"],
            description = data["description"]
        )