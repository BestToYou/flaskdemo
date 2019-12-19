from flask import Flask
#本句话引入数据模型

from app.models.base import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)


    #数据模型的初始化
    db.init_app(app)
    #数据模型的创建，在数据库中可以体现
    with app.app_context():
        db.create_all(app=app)

    return app

def register_blueprint(app):
    from app.web import  web
    app.register_blueprint(web,url_prefix='/web',)