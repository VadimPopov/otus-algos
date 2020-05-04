from pathlib import Path


class Tester:

    def __init__(self, func, path):
        self.func = func
        self.path = Path(path)
        self.input = self.get_contents('*.in')
        self.expected = self.get_contents('*.out')

    def get_contents(self, pattern):
        for p in self.path.glob(pattern):
            yield p.read_text().strip()

    def test(self, answer, expected):
        return str(answer) == expected

    def run_tests(self):
        for num, (inp, ans) in enumerate(zip(self.input, self.expected)):
            result = self.test(self.func(inp), ans)
            print(f'Test {num} - {result}')
