
'''Add some missing HttpResponse sub-classes'''
from django.http import *

from functools import partial

HttpResponseCreated = partial(HttpResponse, status=201)
HttpResponseAccepted = partial(HttpResponse, status=202)
HttpResponseNoContent = partial(HttpResponse, status=204)
HttpResponseResetContent = partial(HttpResponse, status=205)
HttpResponsePartialContent = partial(HttpResponse, status=206)

import json

class JsonResponse(HttpResponse):
    '''Handy shortcut for dumping JSON data'''
    def __init__(self, content, *args, **kwargs):
        kwargs.setdefault('content_type', 'application/json')
        super(JsonResponse, self).__init__(json.dumps(content), *args, **kwargs)
