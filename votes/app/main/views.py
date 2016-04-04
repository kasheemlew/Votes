# coding: utf-8
from . import main
from flask import render_template, request, redirect, url_for, session, make_response
from . import main
from app import db
from app.models import Vote, Item, User
from geetest import GeetestLib
import json
import random


captcha_id = "b46d1900d0a894591916ea94ea91bd2c"
private_key = "36fc3fe98530eea08dfc6ce76e3d24c4"


@main.route('/', methods=['GET', 'POST'])
def index():
    votes = Vote.query.all()
    return render_template('index.html', votes=votes)


@main.route('/vote/<int:id>/', methods=['GET', 'POST'])
def vote(id):
    vote = Vote.query.get_or_404(id)
    if request.method == 'POST':
	for iid in request.form.values():
            item = Item.query.get_or_404(iid)
            item.count += 1
            db.session.add(item)
            db.session.commit()
        return redirect(url_for('main.result', id=vote.id))
    return render_template('vote1.html', vote=vote)


@main.route('/result/<int:id>/')
def result(id):
    vote = Vote.query.get_or_404(id)
    sorteditems = sorted(vote.item, key= lambda item: item.count, reverse=True)
    return render_template('result.html', vote=vote, sorteditems=sorteditems)


@main.route('/introduction/<int:id>/')
def introduction(id):
    item = Item.query.get_or_404(id)
    return render_template('introduction.html', item=item)


@main.route('/getcaptcha', methods=["GET"])
def get_captcha():
    user_id = random.randint(1,100)
    gt =  GeetestLib(captcha_id, private_key)
    status = gt.pre_process(user_id)
    session[gt.GT_STATUS_SESSION_KEY] = status
    session["user_id"] = user_id
    response_str = gt.get_response_str()
    return response_str


@main.route('/validate', methods=["POST"])
def validate_capthca():
    gt = GeetestLib(captcha_id, private_key)
    challenge = request.form[gt.FN_CHALLENGE]
    validate = request.form[gt.FN_VALIDATE]
    seccode = request.form[gt.FN_SECCODE]
    status = session[gt.GT_STATUS_SESSION_KEY]
    user_id = session["user_id"]
    if status:
        result = gt.success_validate(challenge, validate, seccode, user_id)
    else:
        result = gt.failback_validate(challenge, validate, seccode)
    if result:
        return redirect(url_for('main.index'))


@main.route('/login/')
def login():
    return render_template('login.html')
