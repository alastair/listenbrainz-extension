from redis import Redis


class RedisService:
    def __init__(self, app=None):
        self.redis = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.redis = Redis(app.config.REDIS_HOST)
