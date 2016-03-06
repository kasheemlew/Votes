from flask import g, jsonify, request
from flask.ext.httpauth import HTTPBasicAuth
from . import api
from app.models import Permission, Vote, Item, User, Role
import json
from app import db
from .authentication import auth


@api.route('/items/<int:id>', methods=['GET', 'POST'])
def add_one(id):
    item = Item.query.get_or_404(id)
    item.selected += 1
    db.session.add(item)
    db.session.commit()
    return jsonify({
        'now': item.selected
    }), 201


@api.route('/votes/')
def get_votes():
    page = request.args.get('page', 1, type=int)
    pagination = Vote.query.paginate(
            page, per_page=10, error_out=False)
    votes = pagination.items
    return json.dumps(
            [vote.to_json() for vote in votes],
            indent = 1
        ), 200


@api.route('/votes/', methods=['GET', 'POST'])
@auth.login_required
def new_vote():
    vote = Vote.from_json(request.json)
    db.session.add(vote)
    db.session.commit()
    return jsonify({
        'created_vote': vote.id
    })

@api.route('/votes/<int:id>', methods=['GET', 'DELETE'])
@auth.login_required
def delete_vote(id):
    vote = Vote.query.get_or_404(id)
    db.session.delete(vote)
    db.session.commit()
    return jsonify({
        'deleted': vote.id
        }), 200

@api.route('/items/', methods=['GET', 'POST'])
@auth.login_required
def new_item():
    item = Item.from_json(request.json)
    db.session.add(item)
    db.session.commit()
    return jsonify({
        'created_item': item.id
    })
