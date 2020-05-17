import sys
sys.path.append('..')

from helpers import arg_parser


@arg_parser
def king_bitboard(n):
    # current position on bitboard
    pos = 1 << n
    # masks of positions from which king can and can't move left or right
    # next position will be equal to pos << value or pos >> value for a valid move and 0 otherwise
    all_except_col_a = 0xFEFEFEFEFEFEFEFE
    all_except_col_h = 0x7F7F7F7F7F7F7F7F
    # prevents jumps over board top/bottom
    mask_64bit = 0xFFFFFFFFFFFFFFFF
    mask = (
        all_except_col_h & (pos << 7 | pos >> 1 | pos >> 9) | # king moves up/down and left or simply left
        all_except_col_a & (pos << 9 | pos << 1 | pos >> 7) | # king moves up/down and right or simply right
        mask_64bit       & (pos << 8            | pos >> 8)   # king moves up or down
    )
    mask_tmp = mask
    num_possible_moves = 0
    # counting the number of set bits in mask, which will yield the number of possible moves
    while mask_tmp:
        num_possible_moves += 1
        # unsetting the rightmost set bit
        mask_tmp &= mask_tmp - 1
    return '\n'.join(map(str, [num_possible_moves, mask]))


if __name__ == '__main__':
    from tester import Tester

    tester = Tester(king_bitboard, r'6.BITS\1.Bitboard - Король')
    tester.run_tests()
