class OpenAiClass():
    def __init__(self, client):
        self.client = client

        # this will change later when we know what we need as a system prompt
        self.system = """
        Act as a moderator for democratic discussions on controversial and popular topics.
        Yes or no questions on controversial topics will be asked to users who can then write discussion posts on their opinions.
        Use the discussions and replies of the user to generate a follow up question about topics users find important about the issue.
        The generated questions should be related to the original question.
        The generated questions must be questions that are answered by yes or no.
        The generated questions must be clear, short and concise and easy to understand for general people.
        Do not add any pretext to the response, only provide the generated question.
        The generated question must be opinion based and not one that can be answered easily with a fact.
        """

    def new_question_query(self, question, discussions, results_yes, results_no):

        request = "Generate a follow up question based on the following question: " + question + ". The discussions and replies are, each new discussion is seperated by a ***: " + "***".join(discussions) + ". The results are to the question are " + str(results_yes) + " that answered yes and " + str(results_no) + " that answered no."
        print("Request: ", request)
        # Create a reuqest to api and get the completion
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.system},
                {"role": "user", "content": request}
            ]
        )

        return completion.choices[0].message.content