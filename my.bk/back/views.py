
from flask import Blueprint, request, render_template, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash


#验证密码的 jianjiatow

#第一步生成蓝图，用于管理路由
from back.models import User, LanMu, db, WZ
from utils.functions import is_login

back_blue = Blueprint('back',__name__)

#第二步 ： 使用蓝图对象管理路由

#首页
@back_blue.route('/',methods=['GET','POST'])
def home():
    if request.method =='GET':
        return render_template('back/login.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username,password)
        user = User.query.filter(User.name == username).first()
        if not user:
            error = '用户名不存在'
            return render_template('back/login.html',error=error)
        if not check_password_hash(user.password, password):
            error = '密码错误'
            return render_template('back/login.html',error=error)
        session['user_id'] = user.name
        return redirect(url_for('back.index'))

#注册
@back_blue.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('back/register.html')
    if request.method == 'POST':
        #获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        password1 = request.form.get('password1')
        number = request.form.get('number')
        email = request.form.get('email')
        # 判断用户名是否注册过，如果注册在判断密码
        user = User.query.filter(User.name == username).first()
        if user:
            #用户存在
            error = '用户名已存在'
            return render_template('back/register.html', error = error)
        else:
            if password1 == password:
                #保存数据
                user = User()
                user.name = username
                # user.password = password
                #给密码编码
                user.password = generate_password_hash(password)
                user.email = email
                user.number = number
                user.save()
                return redirect(url_for('back.home'))
            else:
                #密码不一样
                error='两次输入的密码不一致'
                return render_template('back/register.html',error=error)

#得到博客主页
@back_blue.route('/index/',methods=['GET'])
@is_login
def index():
    if request.method == 'GET':
        return render_template('back/index.html', error=session.get('user_id'))


@back_blue.route('/delete/',methods=['GET'])
def delete():
    if request.method == 'GET':
        session.pop('user_id')  #删除session
        return redirect(url_for('back.home'))


@back_blue.route('/wenzhang/',methods=['GET','POST'])
@is_login
def wenzhang():
    if request.method == 'GET':
        types = WZ.query.all()
        return render_template('back/add-article.html', error=session.get('user_id'), types=types)
    if request.method == 'POST':
        title = request.form.get('title')
        nr = request.form.get('nr')
        ms = request.form.get('ms')
        if not (title and nr and ms):
            errtr = '请完整输入'
            return render_template('back/add-article.html', errtr=errtr)
        else:
            w = WZ()
            w.title = title
            w.nr = nr
            w.ms = ms
            db.session.add(w)
            db.session.commit()
            return redirect(url_for('back.wenzhang'))



@back_blue.route('/gonggao/',methods=['GET'])
@is_login
def gonggao():
    if request.method == 'GET':
        return render_template('back/add-notice.html',error=session.get('user_id'))

#文章列表
@back_blue.route('/wzlist/',methods=['GET'])
@is_login
def pinglun():
    if request.method == 'GET':
        types = WZ.query.all()
        page = request.args.get('page', 1, type=int)
        pagination = WZ.query.order_by(WZ.create_time.desc()).paginate(page, per_page=2, error_out=False)
        users = pagination.items
        print(pagination)
        print(users)
        return render_template('back/comment.html', error=session.get('user_id'), users=users, pagination=pagination)

#文章删除
@is_login
@back_blue.route('/del_wz/<int:id>/', methods=['GET'])
def del_wz(id):
    #从数据库里找到id一样的一行完整数据，
    type = WZ.query.get(id)
    db.session.delete(type) #删除
    db.session.commit()
    return redirect(url_for('back.pinglun'))

#栏目的添加
@back_blue.route('/lanmu/',methods=['GET','POST'])
@is_login
def lanmu():
    if request.method == 'GET':
        types = LanMu.query.all()
        return render_template('back/category.html', error=session.get('user_id'), types=types)
    if request.method =='POST':
        name = request.form.get('name')
        bm = request.form.get('bm')
        gjz = request.form.get('gjz')
        ms = request.form.get('ms')
        #保存栏目信息
        LM = LanMu()
        LM.id = name
        LM.bieming = bm
        LM.gjz = gjz
        LM.miaoshu = ms
        db.session.add(LM)
        db.session.commit()
        return redirect(url_for('back.lanmu'))

#栏目删除
@is_login
@back_blue.route('/del_lanmu/<string:id>/',methods=['GET'])
def del_type(id):
    #从数据库里找到id一样的一行完整数据，
    atype = LanMu.query.get(id)
    db.session.delete(atype) #删除
    db.session.commit()
    return redirect(url_for('back.lanmu'))

@is_login
@back_blue.route('/xiugai/<string:id>/',methods=['GET','POST'])
def undate_lanmu(id):
    if request.method == 'GET':
        return render_template('back/xiugai.html')
    if request.method == 'POST':
        name = request.form.get('name')
        bm = request.form.get('bm')
        gjz = request.form.get('gjz')
        ms = request.form.get('ms')
        #从数据库里找到id一样的一行数据
        atype = LanMu.query.get(id)
        # print(atype)
        atype.id = name
        atype.bieming = bm
        atype.gjz = gjz
        atype.miaoshu = ms
        #添加  提交
        db.session.add(atype)
        db.session.commit()
        return redirect(url_for('back.lanmu'))







