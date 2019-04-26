import redis
from flask import Flask
from flask_script import Manager
from flask_session import Session

from back.models import db
from back.views import back_blue
from web.views import web_blue

app = Flask(__name__)
# 第三步: 注册蓝图，可以使用蓝图blue管理路由了
app.register_blueprint(blueprint=web_blue,url_prefix='/web')
app.register_blueprint(blueprint=back_blue ,url_prefix='/back')


#连接mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1204@127.0.0.1:3306/xinxi'


#连接redis的方法
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)

# session 此刻存在浏览器里， 可以连接redis数据库，存在数据库里
app.secret_key = '1315456454sdfasdffs'

Session(app)  #配置方法

db.init_app(app)

if __name__ == '__main__':
    manage = Manager(app)
    manage.run()

