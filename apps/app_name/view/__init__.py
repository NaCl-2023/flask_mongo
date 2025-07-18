from .api import API
from .index import INDEX

bps = [INDEX, API]


def init_blue_print(app):
    for bp in bps:
        app.register_blueprint(bp)
