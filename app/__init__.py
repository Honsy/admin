from flask import Flask
from flask_bootstrap import Bootstrap
from  flask_sqlalchemy import SQLAlchemy
from config import config
# 跨域配置
from flask_cors import *



bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    # 处理跨域请求
    CORS(app, supports_credentials=True)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    # 书签 蓝本
    from .bookmark import bookmark as  bm_blueprint
    from .bookmark.auth import bookmarkauth as  bmauth_blueprint
    app.register_blueprint(bm_blueprint,url_prefix = '/bookmark')
    app.register_blueprint(bmauth_blueprint,url_prefix = '/bookmark/auth')

    # 简单记事 藍本
    from .jdjs import jdjs as  jdjs_blueprint
    from .jdjs.auth import jdjsauth as  jdjs_blueprint
    # 前台认证相关蓝图
    app.register_blueprint(jdjs_blueprint,url_prefix = '/jdjs/auth')
    # 后台蓝图
    from .back import back as  back_blueprint
    from .back.auth import backauth as  backauth_blueprint
    from .back.user import backuser as  backuser_blueprint
    app.register_blueprint(back_blueprint,url_prefix = '/back')
    # 后台认证相关蓝图
    app.register_blueprint(backauth_blueprint,url_prefix = '/back/auth')
    # 后台用户相关蓝图
    app.register_blueprint(backuser_blueprint,url_prefix = '/back/user')

    return app