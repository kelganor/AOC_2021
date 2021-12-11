# aoc 2021-11


from itertools import product


def gen_next(matrix):
    H, W = len(matrix), len(matrix[0])
    to_flash, extinct = [], []
    for y in range(H):
        for x in range(W):
            matrix[y][x] += 1
            if matrix[y][x] == 10:
                to_flash.append((y, x))
    flashes = 0
    while to_flash:
        flashes += 1
        y, x = to_flash.pop()
        extinct.append((y, x))
        for dy, dx in product((0, 1, -1), repeat=2):
            yn, xn = y + dy, x + dx
            if 0 <= yn < H and 0 <= xn < W:
                if matrix[yn][xn] == 9:
                    to_flash.append((yn, xn))
                if matrix[yn][xn] < 10:
                        matrix[yn][xn] += 1
    for y, x in extinct:
        matrix[y][x] = 0
    return flashes


def solve(matrix):
    res = sum([gen_next(matrix) for _ in range(100)])
    return res


def solve2(matrix):
    step = 1
    while gen_next(matrix) != len(matrix) * len(matrix[0]):
        step += 1
    return step


if __name__ == "__main__":

    convert = lambda lines: [[int(x) for x in line] for line in lines]

    with open('data/input_11.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    testlines = [
        '5483143223',
        '2745854711',
        '5264556173',
        '6141336146',
        '6357385478',
        '4167524645',
        '2176841721',
        '6882881134',
        '4846848554',
        '5283751526',
    ]
    assert(solve(convert(testlines)) == 1656)
    assert(solve2(convert(testlines)) == 195)

    print('p1: ', solve(convert(lines)))
    print('p2: ', solve2(convert(lines)))
