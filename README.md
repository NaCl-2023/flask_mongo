## 基础flask + mongo的脚手架
更方便的进行常规的flask项目初始化，脱胎于Flask-Application。

### 虚拟环境
- 创建虚拟环境（--python:指定Python版本）：`virtualenv venv --python=python3`
- 激活虚拟环境：`source venv/bin/activate` 
- 退出虚拟环境：`deactivate` 
- 安装库：`pip install -r requirements.txt` 
- 生成req文件：`pip freeze > requirements.txt` 

### 启动
- 启动配置在 conf/config.ini
  - host为 127.0.0.1
  - 端口为 8081
- 非生产环境：`python manage.py`
- 生生产环境：`sh startserver.sh`

### 附带部分框架配置
- nginx配置(可自行link到对应地方)
  - conf/flask_mongo.conf
  - `ln -s /root/projects/ToolServer/conf/tool_server.conf /etc/nginx/server/tool_server.conf`
- gunicorn配置
  - config/gconfig.py
- systemctl配置
  - conf/flask_mongo.service
  - 启动和停止sh startserver.sh/stopserver.sh

