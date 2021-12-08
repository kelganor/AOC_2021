# aoc 2021-05


from collections import Counter


def solve(lines):
    res = 0
    for _, msg in lines:
        for x in msg:
            if len(x) in [2,3,4,7]:
                res += 1

    return res


def solve2(lines):
    """
    define coded numbers by cells used by numbers 1,7,4
    """
    res = 0
    for codes, msg in lines:

        nums = {}
        codes = sorted(codes, key=lambda x: len(x))
        d = {}
        nums[codes[2]] = 4
        nums[codes[1]] = 7
        nums[codes[0]] = 1
        nums[codes[-1]] = 8
        # order matters
        for x in codes[2]: d[x] = '4'
        for x in codes[1]: d[x] = '7'
        for x in codes[0]: d[x] = '1'

        for code in codes:
            numcode = ''
            for x in code:
                if x in d: numcode += d[x]
            c = Counter(numcode)
            if len(code) == 6 and   (c['4'], c['7'], c['1']) == (2, 1, 2):
                nums[code] = 9
            elif len(code) == 6 and (c['4'], c['7'], c['1']) == (2, 1, 1):
                nums[code] = 6
            elif len(code) == 6 and (c['4'], c['7'], c['1']) == (1, 1, 2):
                nums[code] = 0
            elif len(code) == 5 and (c['4'], c['7'], c['1']) == (2, 1, 1):
                nums[code] = 5
            elif len(code) == 5 and (c['4'], c['7'], c['1']) == (1, 1, 1):
                nums[code] = 2
            elif len(code) == 5 and (c['4'], c['7'], c['1']) == (1, 1, 2):
                nums[code] = 3

        msgnum = int(''.join([
            str(nums[m]) for m in msg
        ]))
        res += msgnum

    return res


if __name__ == "__main__":

    with open('data/input_08.txt') as f:
        lines = f.readlines()
    lines = [tuple(map(lambda x: x.split(), x.strip().split(' | '))) for x in lines]
    lines = [
        ([''.join(sorted(c)) for c in codes],
        [''.join(sorted(m)) for m in msg])
        for codes, msg in lines
    ]


    print('p1: ', solve(lines))
    print('p2: ', solve2(lines))
