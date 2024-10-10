# File       : __init__.py
# Time       ：2024/9/30 16:06
# Author     ：nacl
# version    ：python 3.8
# Description：
from configparser import ConfigParser
from dataclasses import dataclass

from utils.file_utils import read_ini


@dataclass
class Common:
    debug: bool
    host: str
    port: int
    salt: str


@dataclass
class Admin:
    username: str
    password: str


@dataclass
class DB:
    host: str
    port: int
    auth_source: str
    username: str
    password: str
    db_name: str


class ConfigModel:
    data: ConfigParser()
    common: Common
    admin: Admin
    db: DB

    def __init__(self):
        self.data = read_ini('./config/config.ini')

        self.common = Common(**self.data['common'])
        self.admin = Admin(**self.data['admin'])
        self.db = DB(**(self.data['db'] if self.common.debug else self.data['db_test']))


Config = ConfigModel()
