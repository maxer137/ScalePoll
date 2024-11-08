from objects.question import Question

class POCQuestionList():
    def __init__(self):
        self.questions = []

        # Example question
        self.questions.append(
            Question("Is this a question?")
        )

    def get_question(self):
        return self.questions[-1]
    
    def add_question(self, question:Question):
        self.questions.append(question)
