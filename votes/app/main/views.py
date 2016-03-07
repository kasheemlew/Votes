# coding: utf-8
from . import main
from flask import render_template
from .forms import VoteForm
from . import main


# test views
@main.route('/test/')
def test():
    return "<h1>just tell you everything is ok!</h1>"


@main.route('/', methods=['GET', 'POST'])
def index():
    form = VoteForm()
    return render_template('index.html', form=form)
