# aoc 2021-17
# ! fits x1, x2 > 0 and y1, y2 < 0


def solve(x1, x2, y1, y2):
    #return sum([x for x in range(y1)])
    return y1 * (y1 + 1) // 2


def move(x1, x2, y1, y2, vx, vy):
    x, y = 0, 0
    while True:
        if x1 <= x <= x2 and y1 <= y <= y2:
            return 1
        if x > x2 or y < y1:
            return 0
        x, y = x + vx, y + vy
        vx = vx - 1 if vx > 0 else 0
        vy -= 1


def solve2(x1, x2, y1, y2):
    vy_h = abs(min(y1, y2))
    vx_h = max(x1, x2)
    res = sum([
        move(x1, x2, y1, y2, vx, vy)
        for vx in range(vx_h+1)
        for vy in range(-vy_h-1, vy_h+1)
    ])
    return res


if __name__ == "__main__":
    # with open('datag/input_17.txt') as f:
    #     lines = f.read().strip().split('\n')

    x1, x2 = 128, 160
    y1, y2 = -142, -88

    print(solve(x1, x2, y1, y2))
    print(solve2(x1, x2, y1, y2))
