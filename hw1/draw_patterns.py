def draw(n=25, cond=None):
    n = int(n)
    for x in range(n):
        for y in range(n):
            print(f"{'#' if eval(cond) else '.'} ", end=' ')
        print('\n')


if __name__ == '__main__':
    with open('patterns.txt') as f:
        for line in f:
            num, cond = line.strip().split('. ')
            print(f'Pattern {num}\n')
            draw(cond=cond)
