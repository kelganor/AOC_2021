# aoc 2021-13


def fold(dots, f):
    res = set()
    axis, q = f
    q = int(q)
    for x, y in dots:
        if axis == 'y':
            res.add((x, y) if y < q else (x, 2 * q - y))
        elif axis == 'x':
            res.add((x, y) if x < q else (2 * q - x, y))
    return res


def solve(dots, folds):
    res = len(fold(dots, folds[0]))
    return res


def solve2(dots, folds):
    for f in folds:
        dots = fold(dots, f)
    xmax, ymax = max([x for x, y in dots]), max([y for x, y in dots])
    code = [[' '] * (xmax+1) for _ in range(ymax+1)]
    for x, y in dots:
        code[y][x] = '■'
    for line in code:
        print(''.join(line))


if __name__ == "__main__":

    with open('data/input_13.txt') as f:
        dlines, flines = f.read().split("\n\n")

    dots = set([tuple(map(int, line.split(','))) for line in dlines.split("\n")])
    folds = [line[11:].split('=') for line in flines.strip().split("\n")]

    print('p1: ', solve(dots, folds))
    print('p2: ')
    solve2(dots, folds)
