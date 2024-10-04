# File       : log_decorator.py
# Time       ：2024/9/26 12:21
# Author     ：nacl
# version    ：python 3.8
# Description：日志装饰器
import functools
import logging

from flask import request


def log(func):
    """
    常规函数log装饰器
    @param func:
    @return:
    """
    name = '[Log Decorator]'

    @functools.wraps(func)  # 将被装饰器覆盖的名字还原回来
    def wrapper(*args, **kwargs):
        text = f"{name} Calling function [{func.__name__}] with arguments: [{args}, {kwargs}]"
        logging.info(text if len(text) < 200 else text[:200] + '...]')
        result = func(*args, **kwargs)
        text = f"{name} Function [{func.__name__}] returned: [{result}]"
        logging.info(text if len(text) < 200 else text[:200] + '...]')
        return result

    return wrapper


def log_request(func):
    """
    请求函数log装饰器。来源地址、请求路由
    :param func:
    :return:
    """
    name = '[Log Request]'

    @functools.wraps(func)  # 将被装饰器覆盖的名字还原回来
    def wrapper(*args, **kwargs):
        ipaddress = request.remote_addr
        method = request.method
        path = request.path

        text = f"{name}[{ipaddress}][function {func.__name__}][method {method}] {path}"
        logging.info(text if len(text) < 200 else text[:200] + '...]')
        result = func(*args, **kwargs)
        text = f"{name} Function [{func.__name__}] returned: [{result}]"
        logging.info(text if len(text) < 200 else text[:200] + '...]')
        return result

    return wrapper


def log_mongodb(func):
    """
    Mongodb日志装饰器
    @param func:
    @return:
    """
    pass