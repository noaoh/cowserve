#!/usr/bin/env python
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher

from pysay.scripts.pysay import cowsay as _cowsay, Appearance


@dispatcher.add_method
def cowsay(cow="default", message="", **app):
    return _cowsay(cow=cow, message=message, a=Appearance(**app))

@dispatcher.add_method
def cowthink(cow="default", message="", **app):
    return _cowsay(cow=cow, message=message, a=Appearance(**app,
        thinking=True))


@Request.application
def application(request):
    response = JSONRPCResponseManager.handle(
            request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


def main():
    run_simple("localhost", 8080, application)


if __name__ == "__main__":
    main()

