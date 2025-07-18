import os

from flask import Blueprint, jsonify, current_app, request

from config.config import BaseConfig
from logger.log_decorator import log_request
from utils import Tools
from utils.request_utils import check_age

APP_NAME = 'app_name'  # Replace with your actual app name
MODULE_NAME = os.path.splitext(os.path.basename(__file__))[0]
API = Blueprint(MODULE_NAME, __name__, url_prefix=f'/{APP_NAME}/{MODULE_NAME}')


@API.route('/', methods=[BaseConfig.GET_TYPE, BaseConfig.POST_TYPE])
@log_request
@check_age(['name', 'password'])  # 参数检查
def api_index():
    current_app.logger.info(f'{request.method} {Tools.fun_stack}')
    if request.method == BaseConfig.GET_TYPE:
        data = request.args
        return jsonify({"success": True, 'data': data})
    else:
        data = request.json  # for request that POST with application/json
        return jsonify({"success": True, 'data': data})
