# File       : account.py
# Time       ：2024/9/9 下午9:17
# Author     ：nacl
# version    ：python 3.10
# Description：账号相关事务
import functools

from flask import jsonify

from utils.request_utils import get_age


def check_account_for_request(is_admin=False):
    """
    身份验证装饰器
    @param is_admin: 是否为admin身份
    @return:
    """

    def inner_wrapper(func):
        @functools.wraps(func)
        def wrapper():
            ages = get_age()
            if 'name' not in ages or 'password' not in ages:
                return jsonify({"success": False, 'msg': '身份验证缺少用户名或密码！'})
            # add 身份验证逻辑


            return func()

        return wrapper

    return inner_wrapper
