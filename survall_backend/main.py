from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from openai import OpenAI
from dotenv import load_dotenv

from endpoints.questions_endpoint import AnswerQuestion, RequestQuestion

from survall import Survall
from endpoints.openai_endpoint import RequestOpenAi

# Load environment variables
load_dotenv()

# Initialize OpenAI
openai = OpenAI()

Survall().setup(openai)

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

# @app.errorhandler(Exception)
# def handle_exception(e):
#     print(e)

#     # You could log the error here, if desired
#     response = {
#         "message": "An internal error occurred. Please try again later."
#     }
#     return response, 500

api.add_resource(RequestQuestion, '/get_question')
api.add_resource(AnswerQuestion, '/post_answer')
api.add_resource(RequestOpenAi, '/get_openai')

if __name__ == '__main__':

    previous_question = "Do you agree with raising the minimum wage?"

    discussions = ["As a small business owner, I worry that raising the minimum wage will stretch my budget to the breaking point. I can’t afford to pay my employees more without having to cut staff or even close up shop.",
                   "When people are paid fairly, they’re happier and more productive at work. A higher minimum wage would reduce turnover and help businesses retain skilled, motivated employees.",
                   "Higher wages could make it harder for young people to get a foot in the door. When entry-level positions are too expensive, employers may stop hiring inexperienced workers, depriving them of valuable job experience.",
                   "If we raise the minimum wage, many low-skilled jobs may be cut because businesses will turn to automation or hire fewer people to save costs. This change could ultimately hurt the very workers it aims to help",
                   "I believe raising the minimum wage is essential to reducing poverty and bridging the income gap. A fair wage would give people the financial security they need to live with dignity.",
                   "Raising the minimum wage could create resentment among workers who have been with us longer. It’s unfair for new hires to make almost as much as experienced employees without pay adjustments across the board.",
                   "A higher minimum wage would help close the wage gap, especially for women and minorities who are overrepresented in low-wage industries. This change would promote a more equitable society.",
                   "If wages go up, fewer people will need to rely on public assistance. This would not only help individuals become more self-sufficient but also save taxpayer money in the long run.",
                   "Every worker deserves a wage that allows them to cover their basic needs. Raising the minimum wage is about giving people a fair shot at a decent life, with dignity and respect in the workplace."]

    num_yes = 80
    num_no = 56

    print(Survall().openai.new_question_query(previous_question, discussions, num_yes, num_no))

    #app.run(host="0.0.0.0",debug=True, port=1337)


        