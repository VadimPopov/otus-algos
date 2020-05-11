import time
from pathlib import Path


class Tester:

    def __init__(self, func, path):
        self.func = func
        self.path = Path(path)
        self.input = self.get_contents('*.in')
        self.expected = self.get_contents('*.out')

    def get_contents(self, pattern):
        fnames = sorted(self.path.glob(pattern), key=lambda f: int(f.name.split('.')[1]))
        for p in fnames:
            yield p.read_text().strip()

    def test(self, answer, expected):
        return str(answer) == expected

    def run_tests(self):
        for num, (inp, exp) in enumerate(zip(self.input, self.expected)):
            start_time = time.time()
            try:
                ans = self.func(inp)
            except RecursionError:
                print(f'Test {num} - Failed due to exceeding maximum recursion depth (to be expected)')
            else:
                result = self.test(ans, exp)
                if result:
                    print(f'Test {num} - {result} - Ran in {time.time() - start_time:.5f} seconds')
                else:
                    print(f'Test {num} - {result} ({ans} != {exp}) - Ran in {time.time() - start_time:.5f} seconds')
