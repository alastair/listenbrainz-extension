# This is kind of "brainzutils cache"

_r = None


def init(redis):
    global _r
    _r = redis


def set(key, value):
    # do some stuff with keys etc
    _r.some_method()
