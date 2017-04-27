#!/usr/bin/python
# -*- coding:utf8 -*-
from flask import render_template
from models import select_all
from models import select_paginate
from jizhuan import app



@app.route('/')
def blank():
    pagination = select_paginate(1)
    return render_template('index.html',title= '三螺旋', pagination= pagination)

@app.route('/all')
def all():
    info_all = select_all()
    return render_template('all.html',title='三螺旋',form=info_all)

@app.route('/index/<int:page>')
def company(page):
    pagination = select_paginate(page)
    return render_template('index.html',title= "三螺旋",pagination=pagination)

@app.route('/order_confirm')
def about():
    return render_template('order_confirm.html')

@app.route('/order_list')
def order():
    return render_template('order_list.html')