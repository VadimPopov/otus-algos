def find_length(string):
    return len(string)


if __name__ == '__main__':
    import sys
    sys.path.append('..')
    from tester import Tester

    tester = Tester(find_length, '0.String')
    tester.run_tests()
