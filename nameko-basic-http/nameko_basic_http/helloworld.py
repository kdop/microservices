# helloworld.py

from nameko.web.handlers import http
import json


class GreetingService:
    name = "greeting_service"

    @http('GET', '/get/<string:value>')
    def hello(self, request, value):
        return json.dumps({'value': value})
