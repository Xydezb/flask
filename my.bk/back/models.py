from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    name = db.Column(db.String(25),primary_key=True)
    password = db.Column(db.String(255),nullable=False)
    number = db.Column(db.String(25),nullable=False)
    email = db.Column(db.String(25),nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)

    __tablename__ = 'yh'

    #保存功能
    def save(self):
        db.session.add(self)
        db.session.commit()


class LanMu(db.Model):
    id = db.Column(db.String(30),primary_key=True)
    bieming = db.Column(db.String(30), nullable=False)
    gjz = db.Column(db.String(50),nullable=False)
    miaoshu = db.Column(db.TEXT,nullable=False)
    __tablename__ = 'lanmu'


class WZ(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    nr = db.Column(db.TEXT,nullable=False)
    ms = db.Column(db.TEXT,nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    __tablename__ = 'wenzhang'










