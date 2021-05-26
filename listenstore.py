from services import db


class ListenStore:

    def get_something(self):
        with db.connection.connect() as connection:
            # do something
            pass