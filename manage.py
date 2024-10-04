import os
import sys

from config import Config


def init_env_path(_file_):
    package_dir = os.path.join(os.path.dirname(_file_), '../')
    abs_path = os.path.abspath(package_dir)
    if abs_path not in sys.path:
        print(f'Add {abs_path} to python path')
        sys.path.insert(0, abs_path)


init_env_path(__file__)

from apps import create_app

__all__ = ['main']


def main():
    app = create_app()

    host = Config.common.host
    port = Config.common.port
    app.run(host, port)


if __name__ == '__main__':
    main()
