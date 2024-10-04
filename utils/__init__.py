import os
import random
import string
from datetime import datetime


def get_abs_dir(_file_):
    return os.path.abspath(os.path.dirname(_file_))


def get_str_time(_datetime: datetime = datetime.now(), time_format: str = '%Y-%m-%d %H:%M:%S'):
    """
    获取格式化日期
    :param _datetime: 待处理的日期
    :param time_format: 格式
    :return:
    """
    if not isinstance(_datetime, datetime):
        return
    return _datetime.strftime(time_format)


def create_random_str(num=8):
    """
    生成特定数量随机字符串(大写和字符串组合)
    :param num: 字符串数量
    :return:
    """
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return ran_str.upper()
    

def save_file(url, value):
    # 保存文件
    try:
        with open(url, 'w', encoding='utf-8') as f:
            f.write(value)
    except:
        return False
    return True
