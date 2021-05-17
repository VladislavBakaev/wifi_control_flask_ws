import json
import pathlib
import os

def get_param():
    wifi_path = pathlib.Path(__file__).parent.parent.absolute()
    file_name = os.path.join(str(wifi_path), 'config_ws.json')

    with open(file_name) as f:
        data = json.load(f)

    return data['wifi_rate']