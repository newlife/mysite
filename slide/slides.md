# ![django](../logo-django.42234b631760.svg)
#### The web framework for perfectionists with deadlines

---
## 三个功能

* url routing

* template

* orm

---

    #!/usr/bin/env python
    import os
    import sys

    if __name__ == "__main__":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        execute_from_command_line(sys.argv)

---
####  从`management`开始

* find_commands

* load_command_class

* get_commands

* call_command

* ManagementUtility

* execute_from_command_line

***

#### Command和他的子类们

* template method (dp)

* startproject

* runserver

---
### startproject

* just copy

* template 出现了

---

### runserver

###### [wsgi](https://www.python.org/dev/peps/pep-0333/#the-application-framework-side){:target="_blank"}

    def simple_app(environ, start_response):
        """Simplest possible application object"""
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return ['Hello world!\n']

---

### runserver

###### [wsgi](https://www.python.org/dev/peps/pep-0333/#the-application-framework-side){:target="_blank"}

`django/core/handlers/wsgi.py`

    class WSGIHandler(base.BaseHandler):
        def __call__(self, environ, start_response):
            request = self.request_class(environ)
            response = self.get_response(request)

            status = '%d %s' % (response.status_code, response.reason_phrase)
            response_headers = list(response.items())
            for c in response.cookies.values():
                response_headers.append(('Set-Cookie', c.output(header='')))
            start_response(status, response_headers)

            if getattr(response, 'file_to_stream', None) is not None and environ.get('wsgi.file_wrapper'):
                response = environ['wsgi.file_wrapper'](response.file_to_stream)
            return response

***
### routing

`django/core/handlers/base.py`

    def _get_response(self, request):
        """
        Resolve and call the view, then apply view, exception, and
        template_response middleware. This method is everything that happens
        inside the request/response middleware.
        """
        if hasattr(request, 'urlconf'):
            urlconf = request.urlconf
            set_urlconf(urlconf)
            resolver = get_resolver(urlconf)
        else:
            resolver = get_resolver()
        resolver_match = resolver.resolve(request.path_info)
        callback, callback_args, callback_kwargs = resolver_match
        request.resolver_match = resolver_match


---

[8888](http://localhost:8888){:target="_blank"}
