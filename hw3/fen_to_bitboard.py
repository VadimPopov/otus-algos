def fen_parser(n):
    cur_pos = 0
    counts = {
        'white': {
            'P': 0,
            'N': 0,
            'B': 0,
            'R': 0,
            'Q': 0,
            'K': 0
        },
        'black': {
            'p': 0,
            'n': 0,
            'b': 0,
            'r': 0,
            'q': 0,
            'k': 0
        }
    }
    groups = n.split('/')[::-1]
    for group in groups:
        for element in group:
            if element.isdigit():
                cur_pos += int(element)
            else:
                counts['white' if element.isupper() else 'black'][element] += 1 << cur_pos
                cur_pos += 1
    res = []
    for figures in counts.values():
        for cnt in figures.values():
            res.append(str(cnt))
    return '\n'.join(res)


if __name__ == '__main__':
    import sys
    sys.path.append('..')

    from tester import Tester

    tester = Tester(fen_parser, r'6.BITS\3.Bitboard - FEN')
    tester.run_tests()
