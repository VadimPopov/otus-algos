import sys
sys.path.append('..')

from helpers import arg_parser

@arg_parser
def gcd_subtraction(a, b):
    while a != b:
        if a > b:
            a -= b
        elif b > a:
            b -= a
    return a

@arg_parser
def gcd_modulo(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        elif b > a:
            b %= a
    return max(a, b)

@arg_parser
def gcd_binary(a, b):
    shift = 0
    if a == 0 or b == 0:
        return max(a, b)
    while ((a | b) & 1) == 0:
        shift += 1
        a >>= 1
        b >>= 1
    while (a & 1) == 0:
        a >>= 1
    while b != 0:
        while (b & 1) == 0:
            b >>= 1
        if a > b:
            a, b = b, a
        b -= a
    return a << shift


if __name__ == '__main__':
    from tester import Tester

    algos = [
        (gcd_subtraction, 'subtraction-based'),
        (gcd_modulo, 'modulo-based'),
        (gcd_binary, 'binary')
    ]

    for algo, desc in algos:
        print(f'\nResults for {desc} algorithm\n')
        tester = Tester(algo, '2.GCD')
        tester.run_tests()
