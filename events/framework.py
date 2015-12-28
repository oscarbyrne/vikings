__all__ = ['fetch', 'choose_from', 'trigger']
from common import weighted_choice


def fetch(name):
    from . import definitions
    return getattr(definitions, name)

def choose_from(gstate, events):
    weights = [event.prob(gstate) for event in events]
    return weighted_choice(zip(events, weights))

def trigger(gstate, event):
    event.do(gstate)
    if event.children:
        child = choose_from(gstate, event.children)
        trigger(gstate, child)

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
        cls.parents = tuple(fetch(name) for name in cls.parents)
        for parent in cls.parents:
            parent.children = parent.children + (cls,)


class Event(object, metaclass=EventMeta):

    parents = []

    def do(gstate):
        pass

    def prob(gstate):
        pass
