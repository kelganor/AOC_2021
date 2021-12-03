# aoc 2021-03


def solve(lines):
    n = len(lines)
    count1s = [0] * len(lines[0])
    for line in lines:
        for i, x in enumerate(line):
            if x == '1':
                count1s[i] += 1
    r1 = ''.join(['1' if x / n > 0.5 else '0' for x in count1s])
    return r1


def solve2(lines, r=0):
    w = len(lines[0])
    for j in range(w):
        if len(lines) == 1:
            return lines[0]
        count1 = 0
        for line in lines:
            if line[j] == '1':
                count1 += 1
        t = ((1 if count1 * 2 >= len(lines) else 0) + r) % 2
        lines = [line for line in lines if line[j] == str(t)]
    return None


if __name__ == "__main__":

    with open('data/input_03.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    x = solve(lines)
    y = ''.join(['1' if a == '0' else '0' for a in x])
    print(int(x, 2) * int(y, 2))

    w = solve2(lines[:], r=0)
    z = solve2(lines[:], r=1)
    print(int(w, 2) * int(z, 2))
