from flask import Flask, Response
from inference_service import classification_service
from index_service import index_service
import logging



def setup_app():
    """
    Setup flask application and register blue prints
    :return: The flask app instance
    """
    new_app = Flask(__name__)
    new_app.register_blueprint(index_service)
    new_app.register_blueprint(classification_service)
    return new_app


app = setup_app()


# GUNICORN mode
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
else:
    app.run(port=5000)
