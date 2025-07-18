import os

from flask import Blueprint, current_app, render_template, request

import logger
from apps.app_name.controller.account import check_account_for_request
from config.config import BaseConfig
from logger.log_decorator import log_request
from utils import get_abs_dir
from utils.request_utils import check_age, get_age

APP_NAME = 'app_name'  # Replace with your actual app name
MODULE_NAME = os.path.splitext(os.path.basename(__file__))[0]
INDEX = Blueprint(
    MODULE_NAME, __name__,
    url_prefix=f'/{APP_NAME}/{MODULE_NAME}',
    template_folder=os.path.join(get_abs_dir(__file__), '../templates')
)


@INDEX.route('/', methods=[BaseConfig.GET_TYPE, BaseConfig.POST_TYPE])
@log_request
def index_home():
    current_app.logger.info(f'{request.method} for index.home')
    if request.method == BaseConfig.GET_TYPE:
        name = request.args.get('name', 'Python')
        return render_template('home.html', name=name)  # return html Content
    else:
        name = request.form.get('name', 'Python')  # for request that POST with application/x-www-form-urlencoded
        return f"Hello {name}", 200  # return plain text Content


@INDEX.route('/test', methods=[BaseConfig.GET_TYPE, BaseConfig.POST_TYPE])
@log_request
def test():
    current_app.logger.info(f'{request.method} for index.home')
    logger.info('this is log test')
    logger.warning('this is log test warning')
    logger.error('this is log test error')

    return f"Hello {1}", 200


@INDEX.route('/login', methods=[BaseConfig.GET_TYPE, BaseConfig.POST_TYPE])
@log_request
@check_age(['name', 'password'])  # 参数检查
@check_account_for_request  # 登录验证
def login():
    current_app.logger.info(f'{request.method} for index.login')

    ages = get_age()
    name = ages['name']

    return render_template('home.html', name=name)
