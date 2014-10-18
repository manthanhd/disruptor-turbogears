import datetime
from ming.odm import FieldProperty
from ming.odm.declarative import MappedClass
from ming import schema as s
from disruptorturbogears.model import DBSession


class ArduinoModel(MappedClass):
    class __mongometa__:
        session = DBSession
        name = 'arduino'
        unique_indexes = [('_id',),
                          ('temperature_dump',),
                          ('light_dump',),]
        indexes = [('name',),]

    _id = FieldProperty( s.ObjectId )

    arduino_id = FieldProperty(s.String, required = True)
    temperature_dump = FieldProperty(s.Anything, if_missing=[])
    light_dump = FieldProperty(s.Anything, if_missing=[])

    position = FieldProperty( [s.Float], if_missing=None)
