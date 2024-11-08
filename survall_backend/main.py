from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from endpoints.template_endpoint import TemplateEndpoint

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

api.add_resource(TemplateEndpoint, '/template_get')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=1337)