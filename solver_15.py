# aoc 2021-15


import heapq


def make_neighbs(p, grid):
    res = []
    for axis in range(len(p)):
        for dr in (-1, 1):
            v = tuple(p[:axis] + (p[axis] + dr, ) + p[axis + 1:])
            if v in grid:
                res.append(v)
    return res


def solve(grid, s, t):
    d = {k:float('inf') for k in grid}
    d[s] = 0
    to_visit = set([s])
    tv_heap = []
    heapq.heappush(tv_heap, (0, s))
    visited = set()

    while to_visit:
        dp, p = heapq.heappop(tv_heap)
        if p not in to_visit:
            continue
        to_visit.remove(p)
        visited.add(p)
        for n in make_neighbs(p, grid):
            if n not in visited and d[n] > d[p] + grid[n]:
                d[n] = dp + grid[n]
                to_visit.add(n)
                heapq.heappush(tv_heap, (d[n], n))
    return d[t]


if __name__ == "__main__":
    with open('data/input_15.txt') as f:
        lines = f.read().strip().split('\n')

    h, w = len(lines), len(lines[0])

    grid = {
        (y, x): int(el)
        for y, line in enumerate(lines)
        for x, el in enumerate(line)
    }
    s, t = (0, 0), (h-1, w-1)
    print('p1: ', solve(grid, s, t))


    grid = {
        (y + h * ty, x + w * tx): (int(el) + ty + tx - 1) % 9 + 1
        for y, line in enumerate(lines)
        for x, el in enumerate(line)
        for ty in range(5)
        for tx in range(5)
    }
    s, t = (0, 0), (5 * h - 1, 5 * w - 1)
    print('p1: ', solve(grid, s, t))
