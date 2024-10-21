import random as rd


def gen_random(num_count, begin, end):
    return [rd.randint(begin, end) for _ in range(num_count)]
