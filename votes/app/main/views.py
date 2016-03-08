# coding: utf-8
from . import main
from flask import render_template
from .forms import VoteForm
from . import main
from app import db
import json


# test views
@main.route('/test/')
def test():
    return "<h1>just tell you everything is ok!</h1>"


@main.route('/', methods=['GET', 'POST'])
def index():
    form = VoteForm()
    return render_template('index.html', form=form)

@main.route('/submit/<int:id>', methods=['GET', 'POST'])
def submit(id):
    item = Iterm.query.get_or_404(id)
    item.selected += 1
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('main.index'))
