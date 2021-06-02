from setuptools import setup

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

reqs = parse_requirements('requirements.txt')

setup(
    name="wifi_control_flask_ws",
    version="1.0.0",
    description="Web server for wifi corol",
    py_modules=["ws_app", "http_app"],
    packages=["ws_control", "http_control", "wificontrol_pkg"],
    package_data={"ws_control": ["rate_config_ws.json"]},
    install_requires=reqs
)
