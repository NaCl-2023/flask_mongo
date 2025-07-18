class BaseConfig:
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]flask_app/'
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'

    LOG_DIR = './logs/'

    GET_TYPE = 'GET'  # 默认请求方式
    POST_TYPE = 'POST'  # 默认请求方式


class DBCollection:
    # collection
    pass


class DefaultConfig:
    # 业务配置
    TEMP_USER_EFFECTIVE_TIME = 60*60*24*1  # 临时用户有效时间，默认1天
    
    # identity
    IDENTITY_ADMIN = 'admin'
    IDENTITY_USER = 'user'
