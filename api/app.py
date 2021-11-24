from flask import Flask
from api.config import *

def create_app(*, config_object) -> Flask:
    """Create a flask app instance."""

    flask_app = Flask('mod_api')
    flask_app.config.from_object(config_object)

    from api.controller import route_app
    flask_app.register_blueprint(route_app)

    return flask_app
