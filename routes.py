from flask import Blueprint

import cache
from services import db, listenstore, redis

bp = Blueprint('test', __name__, url_prefix='/')


@bp.route('/')
def hello():
    return "root"
    listenstore.get_something()


@bp.route('/hello')
def hello():
    return "hello"
    redis.redis.set("foo", "bar")
    cache.set("foo", "bar")
    with db.connection.connect() as connection:
        pass
