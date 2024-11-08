import uuid


class Question():
    def __init__(self, text):
        self.text = text
        self.uuid = str(uuid.uuid4())

    def to_dict(self):
        return {
            "text": self.text,
            "uuid": self.uuid
        }

    def to_json(self):
        return self.to_dict()