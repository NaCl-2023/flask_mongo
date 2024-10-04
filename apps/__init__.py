from flask import Flask

from config.config import BaseConfig
from logger import config_log
from .app_name import init_blue_print


def create_app():
    config_log()
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    init_blue_print(app)

    return app
