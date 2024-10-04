# File       : __init__.py.py
# Time       ：2024/9/8 上午12:40
# Author     ：nacl
# version    ：python 3.7
# Description：db相关
from pymongo import MongoClient

from config import Config
from logger.log_decorator import log


class DBConnect:
    """
    基础mongodb连接
    """
    client = MongoClient("mongodb://{username}:{password}@{host}:{prot}/?authSource={auth_source}".format(
        username=Config.db.username,
        password=Config.db.password,
        host=Config.db.host,
        prot=Config.db.port,
        auth_source=Config.db.auth_source
    ))
    db = client[Config.db.db_name]


class BaseCollection(DBConnect):
    """
    基础账号集合
    """
    def __init__(self, collection_name):
        super().__init__()
        self.collection_name = collection_name
        self.collection = self.db[self.collection_name]

    @log
    def find(self, query):
        return self.collection.find(query)

    @log
    def insert_one(self, data):
        return self.collection.insert_one(data).inserted_id

    @log
    def update_one(self, query, new_values):
        """
        修改单条数据
        :param query: 对应查询，如{ "alexa": "10000" }
        :param new_values: 对应值，如 { "alexa": "12345" }
        :return:
        """
        return self.collection.update_one(query, {"$set": new_values})

    @log
    def find_one(self, query):
        return self.collection.find_one(query)
        
    @log
    def update_many(self, data_filter, update):
        """
        更新多个数据
        @param data_filter: 数据筛选器
        @param update: 更新内容
        @return:
        """
        return self.collection.update_many(data_filter, update)


