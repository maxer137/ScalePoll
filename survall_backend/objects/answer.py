import uuid


class Answer():
    def __init__(self, question_uuid, user_uuid, answer_score, relevance_score, discussion):
        if question_uuid is None:
            self.question_uuid = uuid.uuid4()
        else:
            self.question_uuid = uuid.UUID(question_uuid)

        if user_uuid is None:
            self.user_uuid = uuid.uuid4()
        else:
            self.user_uuid = uuid.UUID(user_uuid)

        self.answer_score = answer_score
        self.relevance_score = relevance_score
        self.discussion = discussion

    def to_dict(self):
        return {
            "question_uuid": str(self.question_uuid),
            "user_uuid": str(self.user_uuid),
            "answer_score": self.answer_score,
            "relevance_score": self.relevance_score,
            "discussion": self.discussion,
        }

    def to_json(self):
        return self.to_dict()
    
    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            question_uuid=data["question_uuid"],
            user_uuid=data["user_uuid"],
            answer_score=data["answer_score"],
            relevance_score=data["relevance_score"],
            discussion=data["discussion"]
        )