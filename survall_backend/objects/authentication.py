import uuid
from sqlalchemy import Column, String

from database.sql_base import Base

class Authentication(Base):
    __tablename__ = 'authentication'
    
    session_token = Column(String, primary_key=True, nullable=False)
    user_hash = Column(String, nullable=False)
    
    def __init__(self, user_hash):
        self.session_token = str(uuid.uuid4())
        self.user_hash = user_hash

    def to_json(self):
        return {
            "token": self.session_token
        }