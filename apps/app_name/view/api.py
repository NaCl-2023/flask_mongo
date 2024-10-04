from flask import Blueprint, jsonify, current_app, request

from logger.log_decorator import log_request
from utils.request_utils import check_age

api = Blueprint('api', __name__, url_prefix='/app_name/api')


@api.route('/', methods=['Get', 'Post'])
@log_request
@check_age(['name', 'password'])  # 参数检查
def api_index():
    current_app.logger.info(f'{request.method} api.index')
    if request.method == 'Get':
        data = request.args
        return jsonify({"success": True, "name": 'api.index', 'data': data})
    else:
        data = request.json  # for request that POST with application/json
        return jsonify({"success": True, "name": 'api.index', 'data': data})
