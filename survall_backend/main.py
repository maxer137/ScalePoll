from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from openai import OpenAI
from dotenv import load_dotenv

from openai_singleton import OpenAiSingleton

from endpoints.template_endpoint import TemplateEndpoint

# Load environment variables
load_dotenv()

# Initialize OpenAI
openai = OpenAI()
OpenAiSingleton().setup(openai)

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

api.add_resource(TemplateEndpoint, '/template_get')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=1337)