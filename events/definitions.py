from .framework import Event


class A(Event):

    parents = []

    def do(gstate):
        print 'A'

    def prob(gstate):
        return 0.7

class B(Event):

    parents = ['A']

    def do(gstate):
        print 'B'

    def prob(gstate):
        return 0.9

class C(Event):

    parents = ['A']

    def do(gstate):
        print 'C'

    def prob(gstate):
        return 0.8
