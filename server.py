from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os

#####################
import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)
######################



def hello_world(request):
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "World"
    message = "Good Morning, " + name + "!\n"
    #print(message)
    logger.info(message)
    return Response(message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
