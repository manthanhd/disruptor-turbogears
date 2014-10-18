from tg import expose, lurl
from tg.exceptions import HTTPFound

from disruptorturbogears.lib.base import BaseController
from disruptorturbogears.model.farm import FarmModel


class FarmController(BaseController):

    @expose('disruptorturbogears.templates.farm.field')
    def index(self):
        farm_list=FarmModel.query.find().skip(0).limit(10).all()
        print farm_list
        return dict(page='field', farm_list=farm_list)


    @expose()
    def add_farm(self, came_from=lurl('/farm'), **kw ):
        print kw
        FarmModel(name=kw['name'],
                  area=float(kw['area']),
                  crop_type=kw['type'],
                  field_location_center=[float(kw['latitude']),float(kw['longitude'])]
        )
        return HTTPFound(location=came_from)
