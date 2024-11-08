from flask_restful import Resource, reqparse

class TemplateEndpoint(Resource):
    def get(self):
        return "Test", 418
