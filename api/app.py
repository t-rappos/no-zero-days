from flask import Flask, Blueprint
from flask_restful import Api
from Resources.Hello import Hello
from Resources.Category import CategoryResource
from Resources.todo import Todo
from Resources.Comment import CommentResource
from Resources.event import EventResource
#from Resources.Activity import ActivityResource
#from Resources.Goal import GoalResource
#from Resources.Userimport UserResouce


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Todo, "/todo/<int:id>")
api.add_resource(Hello, '/Hello')
api.add_resource(CategoryResource, '/Category')
api.add_resource(CommentResource, '/Comment')
api.add_resource(EventResource, '/event')
#api.add_resource(ActivityResource, '/activity')
#api.add_resource(GoalResource, '/goal')
#api.add_resource(UserResouce, '/user')