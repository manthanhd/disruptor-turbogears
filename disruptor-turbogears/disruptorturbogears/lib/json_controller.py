from tg import TGController, response
from tg.controllers.decoratedcontroller import _DecoratedControllerMeta
from backlash.tbtools import get_current_traceback
from functools import wraps

class DetectExceptionsMeta(_DecoratedControllerMeta):
    def __init__(cls, name, bases, attrs):
        super(DetectExceptionsMeta, cls).__init__(name, bases, attrs)
        for name, value in attrs.items():
            if hasattr(value, 'decoration'):
                # For each exposed method wrap it to catch exceptions
                # and put back in place the decoration.
                deco = value.decoration
                wrapped_controller = cls.decorate_controller(value, cls._exception)
                wrapped_controller.decoration = deco
                setattr(cls, name, wrapped_controller)

    @classmethod
    def decorate_controller(self, method, error_handler):
        @wraps(method)
        def call(controller, *args, **kw):
            try:
                return method(controller, *args, **kw)
            except Exception as e:
                tb = get_current_traceback()
                tb.log()
                return error_handler(controller, e)
        return call


class JSONResponseController(TGController):
    __metaclass__ = DetectExceptionsMeta

    def _success(self, result):
        return {'code': 0,
                'errors': None,
                'result': result}

    def _failure(self, code, error):
        assert code > 1, 'Failure code must be > 1'
        response.status_int = 400
        return {'code': code,
                'errors': {'error': error}}

    def _exception(self, exception):
        response.status_int = 500
        return {'code': 1,
                'errors': {'exception': str(exception)}}