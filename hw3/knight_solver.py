import sys
sys.path.append('..')

from helpers import arg_parser


@arg_parser
def knight_bitboard(n):
    # current position on bitboard
    pos = 1 << n
    # masks of positions from which knight can and can't move left or right
    # next position will be equal to pos << value or pos >> value for a valid move and 0 otherwise
    all_except_col_a  = 0xFEFEFEFEFEFEFEFE
    all_except_cols_ab = 0xFCFCFCFCFCFCFCFC
    all_except_col_h = 0x7F7F7F7F7F7F7F7F
    all_except_cols_gh = 0x3F3F3F3F3F3F3F3F
    # prevents jumps over board top/bottom
    mask_64bit = 0xFFFFFFFFFFFFFFFF
    # mask listing all possible moves for knight
    mask = (
        all_except_cols_gh & (pos << 6  | pos >> 10) | # knight moves two left and one up/down
        all_except_col_h   & (pos << 15 | pos >> 17) | # knight moves two up/down and one left
        all_except_col_a   & (pos << 17 | pos >> 15) | # knight moves two up/down and one right
        all_except_cols_ab & (pos << 10 | pos >> 6)    # knight moves two right and one up/down
    )
    # intentional 64-bit overflow
    mask &= mask_64bit
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

    tester = Tester(knight_bitboard, r'6.BITS\2.Bitboard - Конь')
    tester.run_tests()
