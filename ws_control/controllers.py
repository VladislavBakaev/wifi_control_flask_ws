
from flask import Blueprint
import time
import gevent
import json
import pathlib
import sys

from ws_control.until import get_param
wifi_path = pathlib.Path(__file__).parent.absolute()
sys.path.insert(0, wifi_path)
import wificontrol_

server = Blueprint('ws', __name__, url_prefix=r'/wifi')

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
