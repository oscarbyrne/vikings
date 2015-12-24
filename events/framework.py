def fetch_event(name):
    import definitions
    return getattr(definitions, name)

class EventMeta(type):

    def __str__(cls):
        return cls.__name__

    def __new__(meta, name, bases, dct):
        dct['children'] = tuple()
        dct['parents']  = tuple(dct['parents'])
        dct['do']   = staticmethod(dct['do'])
        dct['prob'] = staticmethod(dct['prob'])
        return super(EventMeta, meta).__new__(meta, name, bases, dct)

    def __init__(cls, clsname, bases, dct):
        super(EventMeta, cls).__init__(clsname, bases, dct)
        cls.parents = tuple(fetch_event(name) for name in cls.parents)
        for parent in cls.parents:
            parent.children = parent.children + (cls,)


class Event(object):
    __metaclass__ = EventMeta

    parents = []

    def do(gstate):
        pass

    def prob(gstate):
        pass
