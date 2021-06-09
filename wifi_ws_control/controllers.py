
from flask import Blueprint
import time
import gevent
import json
import pathlib
import sys

from wifi_ws_control.until import get_param
from wificontrol_pkg import wificontrol_

server = Blueprint('ws', __name__, url_prefix=r'/ws/wifi')

rate_wifi = get_param()
wifi_control = wificontrol_.WiFiControl()


@server.route('/list')
def action_feedback(ws):
    while not ws.closed:
        try:
            wifi_list = wifi_control.get_all_wifi()
            ws.send(json.dumps({'wifi':wifi_list}))
            gevent.sleep(1/rate_wifi)
        except Exception as e:
            print(e)
            ws.close()
