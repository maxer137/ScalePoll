import json
import uuid

class Question():
    def __init__(self, namespace, text):
        self.text = text
        self.uuid = uuid.uuid5(namespace, self.text)

    def to_dict(self):
        return {
            "text": self.text,
            "uuid": str(self.uuid)  # Convert UUID to a string for JSON compatibility
        }

    def to_json(self):
        return json.dumps(self.to_dict())