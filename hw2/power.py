import sys
sys.path.append('..')
from decimal import Decimal, getcontext
from math import floor, log2

from helpers import arg_parser


@arg_parser
def power_iterative(a, b):
    res = 1
    if isinstance(a, float):
        # built-in floats will suffer from imprecision with this approach, hence decimals
        getcontext().prec = 53
        a = Decimal(a)
    for _ in range(b):
        res *= a
    if isinstance(res, Decimal):
        res = round(res, 27)
    return res

@arg_parser
def power_closest_to_2(a, b):
    if b == 0:
        return 1
    closest_smallest_pow2 = floor(log2(b))
    raised_2 = 2 ** closest_smallest_pow2
    diff = b - raised_2
    if isinstance(a, float):
        getcontext().prec = 53
        a = Decimal(a)
    res = a ** raised_2
    for _ in range(diff):
        res *= a
    if isinstance(res, Decimal):
        res = round(res, 27)
    return res

@arg_parser
def power_binary(a, b):
    res = 1
    if isinstance(a, float):
        getcontext().prec = 53
        a = Decimal(a)
    while b:
        if b % 2 == 1:
            res *= a
        a *= a
        b >>= 1
    if isinstance(res, Decimal):
        res = round(res, 27)
    return res


if __name__ == '__main__':
    from tester import Tester

    algos = [
        (power_iterative, 'iterative'),
        (power_closest_to_2, 'power-of-2-based'),
        (power_binary, 'binary')
    ]

    for algo, desc in algos:
        print(f'\nResults for {desc} algorithm\n')
        tester = Tester(algo, '3.Power')
        tester.run_tests()
