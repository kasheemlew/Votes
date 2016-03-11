# coding: utf-8
from . import main
from flask import render_template, request, redirect, url_for, session
from . import main
from app import db
from app.models import Vote, Item, User
import json


# test views
@main.route('/test/')
def test():
    return "<h1>just tell you everything is ok!</h1>"


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
    return render_template('result.html', vote=vote)


@main.route('/introduction/<int:id>/')
def introduction(id):
    item = Item.query.get_or_404(id)
    return render_template('introduction.html', item=item)
