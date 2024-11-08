from objects.question import Question
from objects.answer import Answer

class MockDatabase():
    def __init__(self):
        self.questions = []
        self.answers = []

    def get_question(self):
        return self.questions[-1]
    
    def get_related_answers(self, question:Question):
        related_answers = []
        for answer in self.answers:
            answer:Answer
            if question.uuid == answer.question_uuid:
                related_answers.append(answer)
        return related_answers

    def add_question(self, question:Question):
        self.questions.append(question)

    def add_answer(self, answer:Answer):
        self.answers.append(answer)

    def _inject_mock_data(self):
        question1 = Question("Do you agree with raising the minimum wage?")
        question2 = Question("Do you agree with the legalization of marijuana?")
        self.questions.append(question1)
        self.questions.append(question2)

        self.answers.append(
            Answer(question_uuid=question1.uuid,
                   user_uuid=None,
                   answer_score=1,
                   relevance_score=1,
                   discussion="A higher minimum wage would help close the wage gap, especially for women and minorities who are overrepresented in low-wage industries. This change would promote a more equitable society.")
        )
        self.answers.append(
            Answer(question_uuid=question1.uuid,
                   user_uuid=None,
                   answer_score=1,
                   relevance_score=0,
                   discussion="")
        )
        self.answers.append(
            Answer(question_uuid=question1.uuid,
                   user_uuid=None,
                   answer_score=-1,
                   relevance_score=1,
                   discussion="Higher wages could make it harder for young people to get a foot in the door. When entry-level positions are too expensive, employers may stop hiring inexperienced workers, depriving them of valuable job experience.")
        )

        self.answers.append(
            Answer(question_uuid=question1.uuid,
                   user_uuid=None,
                   answer_score=1,
                   relevance_score=1,
                   discussion="Legalizing marijuana undercuts the illegal drug market, reducing the power of drug cartels and unregulated dealers. This can lead to safer communities and lower levels of crime.")
        )
        self.answers.append(
            Answer(question_uuid=question1.uuid,
                   user_uuid=None,
                   answer_score=1,
                   relevance_score=0,
                   discussion="")
        )
        self.answers.append(
            Answer(question_uuid=question1.uuid,
                   user_uuid=None,
                   answer_score=-1,
                   relevance_score=1,
                   discussion="Legal marijuana could lead to more cases of driving under the influence, endangering public safety on the roads. It’s challenging to regulate and measure impairment accurately in marijuana-related DUIs.")
        )
