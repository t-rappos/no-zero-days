from flask import request
from flask_restful import Resource
from Model import db, Event, EventSchema
import datetime

events_schema = EventSchema(many=True)
event_schema = EventSchema()


class EventsResource(Resource):
    def get(self):
        events = Event.query.all()
        events = events_schema.dump(events).data
        return {'status': 'success', 'data': events}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = events_schema.load(json_data)
        if errors:
            return errors, 422
        event = Event.query.filter_by(name=data['name']).first()
        if event:
            return {'message': 'Event already exists'}, 400
        event = Event(
            name=json_data['name']
        )

        db.session.add(event)
        db.session.commit()

        result = events_schema.dump(event).data

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = events_schema.load(json_data)
        if errors:
            return errors, 422
        event = Event.query.filter_by(id=data['id']).first()
        if not event:
            return {'message': 'Event does not exist'}, 400
        event.name = data['name']
        db.session.commit()

        result = events_schema.dump(event).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = events_schema.load(json_data)
        if errors:
            return errors, 422
        event = Event.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = events_schema.dump(event).data

        return {"status": 'success', 'data': result}, 204


class EventResource(Resource):
    def get(self, id):
        event = Event.query.get(id) # .filter_by(id=id).first()
        event = event_schema.dump(event).data
        return {'status': 'success', 'data': event}, 200

    def post(self):
        json_data = request.get_json(force=True)
        creation_date = datetime.datetime.now()
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = event_schema.load(json_data)
        if errors:
            return errors, 422
        event = Event.query.filter_by(creation_date=creation_date).first()
        if event:
            return {'message': 'Event already exists'}, 400

        event = Event(
            creation_date=creation_date,
            activity_id=json_data['activity_id'],
            value=json_data['value'],
            comment=json_data['comment'],
        )

        db.session.add(event)
        db.session.commit()

        result = event_schema.dump(event).data
        return {"status": 'success', 'data': result}, 201

    def put(self, id):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = event_schema.load(json_data)
        if errors:
            return errors, 422
        event = Event.query.filter_by(id=id).first()
        if not event:
            return {'message': 'Event does not exist'}, 400

        event.value = data['value'],
        event.comment = data['comment'],

        db.session.commit()

        result = event_schema.dump(event).data

        return {"status": 'success', 'data': result}, 204

'''
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = events_schema.load(json_data)
        if errors:
            return errors, 422
        event = Event.query.filter_by(name=data['name']).first()
        if event:
            return {'message': 'Event already exists'}, 400
        event = Event(
            name=json_data['name']
        )

        db.session.add(event)
        db.session.commit()

        result = events_schema.dump(event).data

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = events_schema.load(json_data)
        if errors:
            return errors, 422
        event = Event.query.filter_by(id=data['id']).first()
        if not event:
            return {'message': 'Event does not exist'}, 400
        event.name = data['name']
        db.session.commit()

        result = events_schema.dump(event).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = events_schema.load(json_data)
        if errors:
            return errors, 422
        event = Event.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = events_schema.dump(event).data

        return {"status": 'success', 'data': result}, 204
        '''