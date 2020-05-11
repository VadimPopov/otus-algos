import sys
sys.path.append('..')
from collections import defaultdict

from helpers import arg_parser


@arg_parser
def find_num_tickets(n, mem=defaultdict(dict)):
    max_digit = 9
    # max sum of digits in left/right half of the ticket of length 2 * n
    max_sum = max_digit * n

    for i in range(max_sum + 1):
        # solve the most trivial case (ticket of length 2)
        if n == 1:
            # for max_sum from 0 to 9, there's only one ticket consisting of two similar digits (e.g., '11' or '77')
            mem[max_sum][i] = 1
        else:
            # for each max_sum from 0 to 9 * n, find the number of possible digit combinations in a ticket half by
            # looking at the previously computed cases for ticket of length n - 1
            num_combos = sum([mem[max_sum - max_digit].get(x, 0) for x in range(i, max(-1, i - max_digit - 1), -1)])
            mem[max_sum][i] = num_combos
    # computed values need to be squared, since they're computed only for a ticket half: x combinations for left half
    # and x combinations for right half is x * x combinations in total
    return sum(v ** 2 for v in mem[max_sum].values())


if __name__ == '__main__':
    from tester import Tester

    tester = Tester(find_num_tickets, '1.Tickets')
    tester.run_tests()
