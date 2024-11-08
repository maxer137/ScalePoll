import uuid

from objects.question_list import POCQuestionList
from openai_class import OpenAiClass

class Survall():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Survall, cls).__new__(cls)
        return cls.instance
    
    def setup(self, openai):
        self.namespace = uuid.uuid4()
        self.question_list = POCQuestionList(self.namespace)
        self.openai = OpenAiClass().setup(openai)