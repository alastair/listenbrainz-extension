from flask import Flask

import cache
from services import db, redis

import routes


def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes.bp)

    # Service configuration
    db.init_app(app)
    redis.init_app(app)
    cache.init(redis.redis)

    return app
