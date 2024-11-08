from survall_backend.utils.mock_database import MockDatabase
from openai_class import OpenAiClass

class Survall():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Survall, cls).__new__(cls)
        return cls.instance
    
    def setup(self, openai):
        self.question_list = MockDatabase()
        self.openai = OpenAiClass(openai)

        self.question_list._inject_mock_data()
