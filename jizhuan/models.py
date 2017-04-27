#!/usr/bin/python
# -*- coding:utf8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from jizhuan import app
from flask_bootstrap import Bootstrap

app.config['SECRET_KEY'] = 'hard to guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/web'#的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名text1
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True #设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app) #实例化
bootstrap = Bootstrap(app)

class Sheet_Form(db.Model):
    __tablename__ = 'sf'
    id = db.Column(db.INTEGER, primary_key=True)
    company = db.Column(db.TEXT)
    url = db.Column(db.TEXT)
    tel = db.Column(db.TEXT)
    fax = db.Column(db.TEXT)
    mail = db.Column(db.TEXT)
    contacts = db.Column(db.TEXT)
    address = db.Column(db.TEXT)
    remarks = db.Column(db.TEXT)


    def __repr__(self):
        return '<Sheet_Form {}'.format(self.company)

def select_id(id):
    if id is not None:
        try:
            info = Sheet_Form.query.filter_by(id= id).first()
            return info
        except IOError:
            return None
        return None

def select_all():
    try:
        info_all = Sheet_Form.query.all()
        return info_all
    except IOError:
        return None
    return None

def select_paginate(page):
    try:
        pagination = Sheet_Form.query.paginate(page, per_page=6, error_out = False)
        return pagination
    except IOError:
        return None
    return None

if __name__ == '__main__':
    abc = select_id(1)
    print abc.company
    print select_id(2).company