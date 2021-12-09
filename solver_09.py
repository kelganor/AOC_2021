# aoc 2021-09


from functools import reduce


def solve(lines):
    h, w = len(lines), len(lines[0])
    res = 0
    for y, line in enumerate(lines):
        for x, el in enumerate(line):
            flag = True
            for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                yn, xn = y + dy, x + dx
                if 0 <= yn < h and 0 <= xn < w:
                    if lines[yn][xn] <= el:
                        flag = False
            if flag:
                res += 1 + int(el)

    return(res)


def fill(mat, point, color):
    n = 0
    h, w = len(mat), len(mat[0])
    to_visit = set([point])
    i = 0
    while to_visit:
        i += 1
        y, x = next(iter(to_visit))
        to_visit.remove((y, x))
        mat[y][x] = color
        n += 1
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            yn, xn = y + dy, x + dx
            if 0 <= yn < h and 0 <= xn < w and mat[yn][xn] == 0:
                to_visit.add((yn, xn))

    return n


def solve2(lines):
    h, w = len(lines), len(lines[0])
    color = 1
    components = {}
    mat = [
        [-1 if x == '9' else 0 for x in line]
        for line in lines
    ]
    for y in range(h):
        for x in range(w):
            if mat[y][x] == 0:
                n = fill(mat, (y, x), color)
                components[color] = n
                color += 1
    top3 = [-1, -1, -1]
    for color in components:
        top3.append(components[color])
        top3 = sorted(top3, reverse=True)[:-1]

    return(reduce(lambda a, b: a * b, top3))


if __name__ == "__main__":

    with open('data/input_09.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    testlines = [
        '2199943210',
        '3987894921',
        '9856789892',
        '8767896789',
        '9899965678',
    ]
    assert(solve(testlines) == 15)
    assert(solve2(testlines) == 1134)

    print('p1: ', solve(lines))
    print('p2: ', solve2(lines))
