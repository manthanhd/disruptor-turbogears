from ming.odm import FieldProperty
from ming.odm.declarative import MappedClass
from ming import schema as s

from disruptorturbogears.model import DBSession


class FarmModel(MappedClass):
    class __mongometa__:
        session = DBSession
        name = 'farms'
        unique_indexes = [('_id',),
                          ('crop_type',),]
        indexes = [('name',),]

    _id = FieldProperty( s.ObjectId )

    name = FieldProperty(s.String)
    crop_type = FieldProperty(s.String)
    field_location_center = FieldProperty([s.Float], if_missing=[])
    area = FieldProperty(s.Float)

    arduino_list = FieldProperty(s.Anything, if_missing=[])

