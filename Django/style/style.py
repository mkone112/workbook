висящая запятая
#облегчает поддержку

80ch docstrings

120ch code

print(
    hello
    there
    )


f-string только простой доступ к attr
    f'{class.attr}'
    bad:
        f'{1+2}'
        f'{func()}'

f-string не должны использоваться для локализуемого текста

избегать We в комментах

можно использовать isort
    # future
    from __future__ import unicode_literals
    
    # standard library
    import json
    from itertools import chain
    
    # third-party
    import bcrypt
    
    # Django
    from django.http import Http404
    from django.http.response import (
        Http404, HttpResponse, HttpResponseNotAllowed, StreamingHttpResponse,
        cookie,
    )
    
    # local Django
    from .models import LogEntry

без переносов строк после отступа в конце docstring

from django.http.response import (
    Http404, HttpResponse, HttpResponseNotAllowed, StreamingHttpResponse,
    cookie,
)

модели
# кастомные методы вроде clean_ должны быть вроде после Meta
    db fields
    custom managers
    Meta
    __str__
    save()
    get_absolute_url

choices style
    class MyModel(models.Model):
        DIRECTION_UP = 'Up'
        DIRECTION_DOWN = 'Down'
        DIRECTION_CHOICES = [
            (DIRECTION_UP, 'Up'),
            (DIRECTION_DOWN, 'Down'),
        ]


print(
    'if this strings',
)

raise Exception(
    'Text'
)