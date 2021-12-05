# aoc 2021-05


def solve(lines):
    d = {}
    for x1, y1, x2, y2 in lines:
        if x1 == x2 and y1 == y2:
            d[(x1, y1)] = d.get((x1, y1), 0) + 1
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                d[(x1, y)] = d.get((x1, y), 0) + 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                d[(x, y1)] = d.get((x, y1), 0) + 1
    res = sum([1 for x in d.values() if x > 1])
    return res


def solve2(lines):
    d = {}
    for x1, y1, x2, y2 in lines:
        dx, dy = x2 - x1, y2 - y1
        if dx != 0: dx = dx/abs(dx)
        if dy != 0: dy = dy/abs(dy)
        x, y = x1, y1
        while x != x2 + dx or y != y2 + dy:
            d[(x, y)] = d.get((x, y), 0) + 1
            x += dx
            y += dy
    res = sum([1 for x in d.values() if x > 1])
    return res


if __name__ == "__main__":

    with open('data/input_05.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    data = []
    for line in lines:
        p1, p2 = line.split(' -> ')
        x1, y1 = map(int, p1.split(','))
        x2, y2 = map(int, p2.split(','))
        data.append((x1, y1, x2, y2))

    print('p1: ', solve(data))
    print('p2: ', solve2(data))
