# coding: utf-8
from . import main
from flask import render_template, request
from . import main
from app import db
import json


# test views
@main.route('/test/')
def test():
    return "<h1>just tell you everything is ok!</h1>"


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/vote1/', methods=['GET', 'POST'])
def vote1():
    return render_template('vote1.html')
