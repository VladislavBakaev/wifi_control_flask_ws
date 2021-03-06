from flask import (
    Blueprint,
    Response, 
    request)
import json
import sys
import pathlib

from wificontrol_pkg import wificontrol_

module = Blueprint('html', __name__, url_prefix=r'/wifi')

wifi_control = wificontrol_.WiFiControl()

@module.route('/connect', methods=['POST'])
def start():
    data = request.json
    res = wifi_control.wifi_connect(data['name'], data['password'])
    return res

@module.route('/forget', methods=['POST'])
def forget():
    data = request.json
    res = wifi_control.del_save_connection(data['name'])
    return res