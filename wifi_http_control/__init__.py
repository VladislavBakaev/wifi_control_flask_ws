from flask import Flask

def create_app():
    app = Flask(__name__)

    import wifi_http_control.controllers as control

    app.register_blueprint(control.module)

    return app