import sys
sys.path.append('..')

from helpers import arg_parser


@arg_parser
def prime_naive(n):
    def is_prime(number):
        for num in range(2, number):
            if number % num == 0:
                return False
        return True
    return sum([is_prime(x) for x in range(2, n + 1)])

@arg_parser
def prime_optimized(n, primes=set()):
    def is_prime(number):
        if number % 2 == 0:
            return number == 2
        sqrt = int(number ** .5)
        if primes:
            arr = filter(lambda prime: prime <= sqrt, primes)
        else:
            arr = range(3, sqrt + 1, 2)
        for num in arr:
            if number % num == 0:
                return False
        primes.add(number)
        return True
    return sum([is_prime(x) for x in range(2, n + 1)])

@arg_parser
def prime_sieve(n):
    lst = [True] * (n + 1)
    num = 2
    while num ** 2 <= n:
        if lst[num]:
            j = num ** 2
            for idx in range(j, n + 1, num):
                lst[idx] = False
        num += 1
    return sum(lst[2:])

@arg_parser
def prime_sieve_linear(n):
    primes = []
    lst = [0] * (n + 1)
    for num in range(2, n + 1):
        if lst[num] == 0:
            lst[num] = num
            primes.append(num)
        try:
            idx = 0
            while primes[idx] <= lst[num] and primes[idx] * num <= n:
                lst[primes[idx] * num] = primes[idx]
                idx += 1
        except IndexError:
            pass
    return len(primes)


if __name__ == '__main__':
    from tester import Tester

    algos = [
        (prime_naive, 'naive'),
        (prime_optimized, 'naive optimized'),
        (prime_sieve, 'Eratosthenes sieve'),
        (prime_sieve_linear, 'linear-complexity Eratosthenes sieve')
    ]

    for algo, desc in algos:
        print(f'\nResults for {desc} algorithm\n')
        tester = Tester(algo, '5.Primes')
        tester.run_tests()
