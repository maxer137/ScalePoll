import re

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
        The generated question should be more specific than the original question, and does not become more general.
        Along with the generated question, provide a short explanation on the relevace of the generated question with regards to the previous one.
        Enclose the generated question within @ symbols.
        Enclose the generated explanation within # symbols.
        """

    def follow_up_question_query(self, question, answers):

        discussions = [answer.discussion for answer in answers]
        results_yes = question.amount_positive
        results_no = question.amount_negative
        results_neutral = question.amount_neutral

        request = "Generate a follow up question based on the following question: " + question.question + ". The discussions and replies are, each new discussion is seperated by a ***: " + "***".join(discussions) + ". The results are to the question are " + str(results_yes) + " that answered yes, " + str(results_no) + " that answered no, and " + str(results_neutral) + " that answered neutrally."
        print("Request: ", request)
        # Create a reuqest to api and get the completion
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.system},
                {"role": "user", "content": request}
            ]
        )

        pattern_question = r'@([^@]+)@'
        pattern_explanation = r'#([^#]+)#'

        gen_question =  re.findall(pattern_question, completion.choices[0].message.content)
        gen_question_explanation = re.findall(pattern_explanation, completion.choices[0].message.content)

        return gen_question, gen_question_explanation