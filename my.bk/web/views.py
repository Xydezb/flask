
from flask import Blueprint, request,\
    render_template, redirect, url_for

#第一步 ：生成蓝图对象
#蓝图用于管理路由
web_blue = Blueprint('first', __name__)



@web_blue.route('/' , methods=['GET'])
def shouye():
    if request.method == 'GET':
        return render_template('web/index.html')


@web_blue.route('/about/',methods=['GET'])
def one():
    if request.method == 'GET':
        return redirect(url_for('first.shouye'))

@web_blue.route('/share/',methods=['GET'])
def two():
    if request.method == 'GET':
        return render_template('web/share.html')
@web_blue.route('/share/',methods=['GET'])
def three():
    if request.method == 'GET':
        return render_template('web/share.html')
@web_blue.route('/share/',methods=['GET'])
def four():
    if request.method == 'GET':
        return render_template('web/share.html')
@web_blue.route('/share/',methods=['GET'])
def five():
    if request.method == 'GET':
        return render_template('web/share.html')