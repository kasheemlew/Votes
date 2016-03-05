from flask import jsonify, request, g, abort, url_for, current_app
from .. import db
from ..models import Iterm, Permission, Role
from . import api
from .decorators import permission_required
from .errors import forbidden


@api.route('/iterms/')
def get_iterms():
    page = request.args.get('page', 1, type=int)
    pagination = Iterm.query.paginate(
            page, per_page=10,
            error_out=False)
    iterms = pagination.iterms
    return json.dumps(
        [iterm.to_json() for iterm in iterms ],
        indent = 1
    ), 200


@api.route('/iterms/<int:id>')
def get_iterms(id):
    iterm = Iterms.query.get_or_404(id)
    return json.dumps(
        [iterm.to_json()],
        indent = 1
    ), 200
