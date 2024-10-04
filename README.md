## 基础flask +　mongo的脚手架
更方便的进行常规的flask项目初始化，脱胎于Flask-Application。

### 虚拟环境
- virtualenv venv --python=python3 # 创建虚拟环境 --python:指定Python版本
- source venv/bin/activate  # 激活虚拟环境
- deactivate # 退出
- pip install -r requirements.txt 安装库
- pip freeze > requirements.txt 生成req文件 

### 启动
- 启动配置在 conf/config.ini
- 默认为8081端口
- host为127.0.0.1
- 非生产环境：python manage.py
- 生生产环境：sh startserver.sh

### 附带部分框架配置
- nginx配置
  - conf/flask_mongo.conf
- gunicorn配置
  - conf/gconfig.py
- systemctl配置
  - conf/flask_mongo.service
  - 启动和停止sh startserver.sh/stopserver.sh

