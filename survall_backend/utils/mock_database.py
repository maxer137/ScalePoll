from objects.question import Question
from survall_backend.objects.answer import Answer

class MockDatabase():
    def __init__(self):
        self.questions = []
        self.answers = []

        # Example question
        self.questions.append(
            Question("Is this a question?")
        )

    def get_question(self):
        return self.questions[-1]
    
    def add_question(self, question:Question):
        self.questions.append(question)

    def add_aswer(self, answer:Answer):
        self.answers.append(answer)
