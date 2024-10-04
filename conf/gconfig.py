import gevent.monkey

gevent.monkey.patch_all()

from config.config import BaseConfig

from config import Config
import multiprocessing

# debug = True
bind = f'{Config.common.host}:{Config.common.port}'
pidfile = f'{BaseConfig.LOG_DIR}/gunicorn.pid'
accesslog = f'{BaseConfig.LOG_DIR}/gaccess.log'
errorlog = f'{BaseConfig.LOG_DIR}/gdebug.log'
loglevel = 'info'
capture_output = True
daemon = True

# 启动的进程数
workers = multiprocessing.cpu_count()
worker_class = 'gevent'
x_forwarded_for_header = 'X-FORWARDED-FOR'
