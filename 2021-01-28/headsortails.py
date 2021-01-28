# base module
import random
import re


def coin_counter(x):
    """
    Flips the coin x times and counts how many times each came out
    """
    total_flips = {}
    heads = 0
    tails = 0
    for i in range(x):
        flipped = random.choice(['heads', 'tails'])
        if flipped == 'heads':
            heads += 1
        else:
            tails += 1
    return {
        'heads': heads,
        'tails': tails
    }

print(coin_counter(5))