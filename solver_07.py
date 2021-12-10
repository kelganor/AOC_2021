# aoc 2021-07


def solve(nums):
    nums = sorted(nums)
    mid = round(len(nums) / 2)
    res = sum([abs(x - nums[mid]) for x in nums])
    return res


def solveBF(nums, cost=lambda x: x):
    res = min([
        sum([ cost(abs(t-x+1)) for x in nums])
        for t in range(min(nums), max(nums))
    ])
    return res


if __name__ == "__main__":

    with open('data/input_07.txt') as f:
        lines = [x.strip() for x in f.readlines()]
    nums = list(map(int, lines[0].split(',')))

    test = [16,1,2,0,4,2,7,1,2,14]
    p2_cost = lambda d: d * (d + 1) // 2
    assert(solve(test) == 37)
    assert(solveBF(test, cost=p2_cost) == 168)

    print(solve(nums))
    print(solveBF(nums, cost=p2_cost))
