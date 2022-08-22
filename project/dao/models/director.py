from marshmallow import Schema, fields
from sqlalchemy import Column, String


from project.setup.db.models import Base


class Director(Base):
    __tablename__ = 'directors'

    name = Column(String(255), unique=True, nullable=False)


class DirectorSchema(Schema):
    ### Схема для сериализации ###
    id = fields.Integer()
    name = fields.String()

