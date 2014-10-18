from webob import Response
from tg import tmpl_context


def report_validation_errors(*args, **kw):
    errors = dict(((str(key), str(error)) for key, error in tmpl_context.form_errors.items()))
    return Response(status=412, json_body={'code': -1,
                                           'result': None,
                                           'errors': errors})
