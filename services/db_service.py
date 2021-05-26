class DBService:
    def __init__(self, app=None):
        self.connection = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        # db postgres connection
        self.connection = 0
