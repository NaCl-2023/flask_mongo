from .api import api
from .index import index

bps = [index, api]


def init_blue_print(app):
    for bp in bps:
        app.register_blueprint(bp)
