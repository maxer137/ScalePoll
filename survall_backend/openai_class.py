class OpenAiClass():
    def setup(self, client):
        self.client = client

        # this will change later when we know what we need as a system prompt
        self.system = """
        Act as a moderator for democratic discussions on controversial and popular topics.

        """

    def new_question_query(self):
        # This can change later to a function parameter once we know better what info we need
        request = "Give me a joke about snakes that must include the word 'Serpentine'"

        # Create a reuqest to api and get the completion
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.system},
                {"role": "user", "content": request}
            ]
        )

        return completion.choices[0].message.content