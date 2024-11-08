import uuid

from objects.question_list import POCQuestionList


class Survall():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Survall, cls).__new__(cls)
        return cls.instance
    
    def setup(self):
        self.namespace = uuid.uuid4()
        self.question_list = POCQuestionList(self.namespace)