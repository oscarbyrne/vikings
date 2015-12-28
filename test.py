import events
from frames import TestFrame

gstate = object()

def step():
    for name in TestFrame.base_events:
        event = events.fetch(name)
        events.trigger(gstate, event)

step()
