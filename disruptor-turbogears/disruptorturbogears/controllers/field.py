from tg import expose, lurl
from tg.exceptions import HTTPFound

from disruptorturbogears.lib.base import BaseController
from disruptorturbogears.model.field import FieldModel


class FieldController(BaseController):

    @expose('disruptorturbogears.templates.field.field')
    def index(self):
        field_list=FieldModel.query.find().skip(0).limit(10).all()
        return dict(page='field', field_list=field_list)


    @expose()
    def add_field(self, came_from=lurl('/field'), **kw ):
        print kw
        FieldModel(name=kw['name'],
                  area=float(kw['area']),
                  crop_type=kw['type'],
                  field_location_center=[float(kw['latitude']),float(kw['longitude'])]
        )
        return HTTPFound(location=came_from)
