# aoc 2021-05


def solve(lines, skip_diags=False):
    d = {}
    for x1, y1, x2, y2 in lines:
        dx, dy = x2 - x1, y2 - y1
        if dx != 0: dx = dx/abs(dx)
        if dy != 0: dy = dy/abs(dy)
        x, y = x1, y1
        while x != x2 + dx or y != y2 + dy:
            if skip_diags and (x1 != x2 and y1 != y2):
                break
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

    print('p1: ', solve(data, skip_diags=True))
    print('p2: ', solve(data))
