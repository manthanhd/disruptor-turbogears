from formencode import validators
from disruptorturbogears.lib.json_controller import JSONResponseController
from tg import expose, validate, url, config
from disruptorturbogears.lib.validators import report_validation_errors

__author__ = 'SilentHK'


class ArduinoController(JSONResponseController):

    @expose('json')
    @validate({'arduino_id': validators.String(not_empty=True),
           'data': validators.String(not_empty=True)},
          error_handler=report_validation_errors)
    def send_data(self,arduino_id=None,data=None, **kw):


        return self._success(dict(some="key"))
