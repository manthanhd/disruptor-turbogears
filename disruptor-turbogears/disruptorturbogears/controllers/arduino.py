import datetime
from formencode import validators
from disruptorturbogears.lib.json_controller import JSONResponseController
from tg import expose, validate, url, config
from disruptorturbogears.lib.validators import report_validation_errors
from disruptorturbogears.model.arduino import ArduinoModel


class ArduinoController(JSONResponseController):

    @expose('json')
    @validate({'device_id': validators.String(not_empty=True),
           'temp': validators.Number(not_empty=True),
           'light': validators.Number(not_empty=True)},
          error_handler=report_validation_errors)

    def send_data(self, device_id=None, temp=None, light=None, **kw):

        arduino = ArduinoModel.query.find({'arduino_id':device_id}).first()
        if arduino is None:
            arduino = ArduinoModel(arduino_id=device_id)
        arduino.temperature_dump.append(dict(value= temp,date = datetime.datetime.utcnow()))
        arduino.light_dump.append(dict(value= light,date = datetime.datetime.utcnow()))

        return self._success({})
