from formencode import validators
from tg import expose, validate
from disruptorturbogears.lib.helpers import generate_authentication_token
from disruptorturbogears.lib.json_controller import JSONResponseController
from disruptorturbogears.lib.validators import report_validation_errors
from disruptorturbogears.model import User


class ApiController(JSONResponseController):


    def get_relevant_data(self):
        return dict()

    @expose('json')
    @validate({'email': validators.String(not_empty=True),
           'password': validators.Number(not_empty=True)},
          error_handler=report_validation_errors)
    def login(self, email=None, password=None,  **kw):
        user = User.query.find({'email_address': email, 'password': password}).first()
        if user is None:
            self._failure(2,'user not found')
        else:
            user.token = generate_authentication_token()

        #return some revelant data for the first screen
        return self._success({'data': self.get_relevant_data()})

    @expose('json')
    @validate({'token': validators.String(not_empty=True)},
          error_handler=report_validation_errors)
    def check_token(self, token=None,  **kw):
        user = User.query.find({'token': token}).first()
        if user is None:
            self._failure(2,'token expired')

        return self._success({'data': self.get_relevant_data()})


    @expose('json')
    @validators({'token': validators.String(not_empty=True)},
          error_handler=report_validation_errors)
    def card_data(self, token, field,  **kw):

        return self._success({})

    # add polling for NOTIFICATIONS every x seconds // ios