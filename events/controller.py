from operator import methodcaller
import random

from .framework import fetch_event


class EventController(object):

    def __init__(self, gstate, prob=1, nchains=3):
        random.seed()
        self.triggered = []
        self.gstate = gstate
        self.prob = prob        #probability multiplier
        self.nchains = nchains  #max number of base events per frame

    def should_trigger(self, event):
        triggered = event in self.triggered
        probable  = event.prob(self.gstate) * self.prob > random.random()
        return not triggered and probable

    def candidates(self, events):
        filtered = filter(self.should_trigger, events)
        return sorted(filtered, key=methodcaller('prob', self.gstate), reverse=True)

    def trigger(self, event):
        self.triggered.append(event)
        event.do(self.gstate)
        candidates = self.candidates(event.children)
        if candidates:
            self.trigger(candidates[0])

    def execute_frame(self, frame):
        candidates = self.candidates(fetch_event(name) for name in frame.base_events)
        number = random.randrange(self.nchains)
        for event in candidates[:number]:
            self.trigger(event)
        self.triggered = []
