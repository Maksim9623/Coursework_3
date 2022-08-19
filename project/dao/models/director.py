from marshmallow import Schema, fields

from project.dao.models.base import BaseModel
from project.setup.db import db


class Director(BaseModel):
    __tablename__ = 'directors'

    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    id = fields.Integer()
    name = fields.String()

