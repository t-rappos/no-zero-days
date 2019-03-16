from flask import Flask, Blueprint
from flask_restful import Api
from Resources.Hello import Hello
from Resources.Category import CategoryResource
from Resources.todo import Todo
from Resources.Comment import CommentResource
from Resources.event import EventResource, EventsResource
from Resources.user import UsersResource, UserEventsResource
#from Resources.Activity import ActivityResource
#from Resources.Goal import GoalResource
#from Resources.Userimport UserResouce


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Todo, "/todo/<int:id>")
api.add_resource(Hello, '/Hello')
api.add_resource(CategoryResource, '/Category')
api.add_resource(CommentResource, '/Comment')
api.add_resource(EventResource, '/event/', '/event/<int:id>')
api.add_resource(EventsResource, '/events')
#api.add_resource(ActivityResource, '/activity')
#api.add_resource(GoalResource, '/goal')
#api.add_resource(UserResouce, '/user')

# /users
# /users/1
api.add_resource(UsersResource, '/users/', '/users/<int:id>')

# /users/1/events
# /users/1/events/1
api.add_resource(UserEventsResource, '/users/<int:user_id>/events/', '/users/<int:user_id>/events/<int:event_id>')

# /users
# /users/1
# /users/1/events
# /users/1/events/1
# /users/1/activities
# /users/1/activities/1
# /users/1/activities/1/events
# /users/1/activities/1/events/1
# /users/1/goals
# /users/1/goals/1
# /users/1/goals/1/activities
# /users/1/goals/1/activities/1
# /users/1/goals/1/activities/1/events
# /users/1/goals/1/activities/1/events/1

