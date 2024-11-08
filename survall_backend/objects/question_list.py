from objects.question import Question

class POCQuestionList():
    def __init__(self, namespace):
        self.namespace = namespace
        self.questions = []

        # Example question
        self.questions.append(
            Question(namespace, "Is this a question?")
        )

    def get_question(self):
        return self.questions[-1]
