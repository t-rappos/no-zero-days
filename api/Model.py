from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id', ondelete='CASCADE'), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(250), nullable=True)
    activity = db.relationship('Activity', backref=db.backref('event', lazy='dynamic'))


class EventSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    creation_date = fields.DateTime()
    activity_id = fields.Integer(required=True)
    value = fields.Integer(required=True)
    comment = fields.String(required=False)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    category = db.relationship('Category', backref=db.backref('comments', lazy='dynamic' ))

    def __init__(self, comment, category_id):
        self.comment = comment
        self.category_id = category_id


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name


class CategorySchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)


class CommentSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    category_id = fields.Integer(required=True)
    comment = fields.String(required=True, validate=validate.Length(1))
    creation_date = fields.DateTime()