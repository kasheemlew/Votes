from flask import g, jsonify, request
from flask.ext.httpauth import HTTPBasicAuth
from ..decorators import admin_required
from . import api
from app.models import Permission, Vote, Iterm, User, Role
import json
from app import db


auth = HTTPBasicAuth()


@api.route('/iterms/<int:id>', methods=['GET', 'POST'])
def add_one(id):
    iterm = Iterm.query.get_or_404(id)
    iterm.selected += 1
    db.session.add(iterm)
    db.session.commit()
    return jsonify(user.to_json()), 201


@api.route('/votes/')
def get_votes():
    page = request.args.get('page', 1, type=int)
    pagination = Vote.query.paginate(
            page, per_page=10, error_out=False)
    votes = pagination.iterms
    return json.dumps(
            [user.to_json() for iterm in iterms],
            indent = 1
        ), 200


@api.route('/votes/', method=['GET', 'POST'])
def new_vote():
    vote = Vote.from_json(request.json)
    db.session.add(vote)
    db.session.commit()
    return jsonify(user.to_json()), 201


@api.route('/votes/<int:id>', methods=['GET', 'DELETE'])
def delete_vote(id):
    vote = Vote.query.get_or_404(id)
    db.session.delete(vote)
    db.session.commit()
    return jsonify({
        'delete': id
        }), 200
