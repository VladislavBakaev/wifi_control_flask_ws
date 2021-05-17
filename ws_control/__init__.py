from flask import Flask
from flask_sockets import Sockets
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
import sys

server = Flask(__name__)

geventOpt = {'GATEWAY_INTERFACE': 'CGI/1.1',
                'SCRIPT_NAME': '',
                'wsgi.version': (1, 0),
                'wsgi.multithread': True, # XXX: Aren't we really, though?
                'wsgi.multiprocess': True,
                'wsgi.run_once': False}

def create_app():
    sockets = Sockets(server)
    ws_server = WSGIServer(('',5000), server, handler_class=WebSocketHandler, environ=geventOpt)
    from ws_control.controllers import server as server_ws
    sockets.register_blueprint(server_ws)

    return ws_server