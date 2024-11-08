from utils.question_list import POCQuestionList
from openai_class import OpenAiClass

class Survall():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Survall, cls).__new__(cls)
        return cls.instance
    
    def setup(self, openai):
        self.question_list = POCQuestionList()
        self.openai = OpenAiClass(openai)
