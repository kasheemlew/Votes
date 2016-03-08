# coding: utf-8
from flask.ext.wtf import Form
from wtforms import RadioField, SubmitField
# from wtforms.validators import


class VoteForm(Form):
    vote = RadioField('Vote 1:', choices=[('A','Option 1'), ('B', 'Option 2')])
    submit = SubmitField('Submit')
