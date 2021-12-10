# aoc 2021-06


from functools import cache
from collections import Counter


@cache
def count(x, days):
    res = 1 if days <= x else count(7, days-x) + count(9, days-x)
    return res


def solve(nums, r):
    d = Counter(nums)
    res = sum([d[x] * count(x, r) for x in d])
    return res


if __name__ == "__main__":

    with open('data/input_06.txt') as f:
        lines = [x.strip() for x in f.readlines()]
    nums = list(map(int, lines[0].split(',')))

    assert(solve([3,4,3,1,2], 17) == len([0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8]))
    assert(solve([3,4,3,1,2], 18) == len([6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8]))
    assert(solve([3,4,3,1,2], 80) == 5934)
    assert(solve([3,4,3,1,2], 256) == 26984457539)

    print(solve(nums, 80))
    print(solve(nums, 256))
