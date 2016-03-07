# coding: utf-8
from flask.ext.wtf import Form
from wtforms import RadioField, SubmitField
# from wtforms.validators import


class VoteForm(Form):
    vote = RadioField('Choice 1:', choices=[('a','Option A'), ('B', 'Option B')])
    submit = SubmitField('Submit')
