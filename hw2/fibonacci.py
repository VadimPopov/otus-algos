import sys
sys.path.append('..')
from decimal import Decimal, getcontext

import numpy as np

from helpers import arg_parser


def fib_recursive(n):
    n = int(n)
    if n < 2:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

@arg_parser
def fib_iterative(n):
    a, b = 0, 1
    for num in range(n):
        a, b = b, a + b
    return a

@arg_parser
def fib_golden_ratio(n):
    getcontext().prec = 53
    phi = Decimal((1 + Decimal(5).sqrt()) / 2)
    return int((phi ** n) / Decimal(5).sqrt() + Decimal(.5))

@arg_parser
def fib_matrix(n):
    res = np.eye(2, dtype='object')
    base = np.ones((2, 2), dtype='object')
    base[1, 1] = 0
    while n:
        if n % 2 == 1:
            res = res @ base
        base = base @ base
        n >>= 1
    return res[1, 0]


if __name__ == '__main__':
    from tester import Tester

    algos = [
        (fib_recursive, 'recursive'),
        (fib_iterative, 'iterative'),
        (fib_golden_ratio, 'golden-ratio-based'),
        (fib_matrix, 'matrix-based')
    ]

    for algo, desc in algos:
        print(f'\nResults for {desc} algorithm\n')
        tester = Tester(algo, '4.Fibo')
        tester.run_tests()
