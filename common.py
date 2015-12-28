from itertools import accumulate
from bisect import bisect
from random import random

def weighted_choice(choices):
    values, weights = zip(*choices)
    cumulative = list(accumulate(weights))
    i = bisect(cumulative, random() * sum(weights))
    return values[i]
