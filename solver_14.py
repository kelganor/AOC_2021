# aoc 2021-14


def gen_next(counter, rules):
    res = {}
    for pair, n in counter.items():
        for gened in rules[pair]:
            res[gened] = res.get(gened, 0) + n
    return res


def solve(counter, rules, steps, lst):
    for _ in range(steps):
        counter = gen_next(counter, rules)
    res = {}
    for pair, n in counter.items():
        res[pair[0]] = res.get(pair[0], 0) + n
    res[lst] += 1
    return max(res.values()) - min(res.values())


if __name__ == "__main__":
    with open('data/input_14.txt') as f:
        template, rules = f.read().strip().split('\n\n')

    rules = map(lambda x: x.strip().split(' -> '), rules.split('\n'))
    rules = {
        pair: (pair[0]+sep, sep+pair[1]) for pair, sep in rules
    }
    counter = {}
    for i in range(len(template)-1):
        p = template[i:i+2]
        counter[p] = counter.get(p, 0) + 1

    print('p1: ', solve(counter, rules, 10, template[-1]))
    print('p2: ', solve(counter, rules, 40, template[-1]))
