from flask import Flask, make_response, jsonify
from instance.config import app_config
import app.api.v1.views.party  as party
import app.api.v1.views.office  as office


def handle_bad_request(e):
    return make_response(
        jsonify(
            {
                "error": "Sorry, request was not understood!",
                "status": 400
            }
        )
    )


def handle_method_not_allowed(e):
    return make_response(
        jsonify(
            {
                "error": "Sorry, request method not allowed",
                "status": 405
            }
        )
    )


def handle_not_found(e):
    return make_response(
        jsonify(
            {
                "error": "The information you are looking for cannot be found",
                "status": 404
            }
        )
    )


def create_app(config_name):
    """ This method creates a flask application """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    app.register_blueprint(party)
    app.register_blueprint(office)
    app.register_error_handler(400, handle_bad_request)
    app.register_error_handler(405, handle_method_not_allowed)
    app.register_error_handler(404, handle_not_found)

    return app