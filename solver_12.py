# aoc 2021-12


from collections import defaultdict


def solve(lines, revisit_allowed=False):
    d = defaultdict(list)
    for line in lines:
        u, v = line.split('-')
        d[u].append(v)
        d[v].append(u)

    unique_pathes = []
    paths = [(set(), True, ['start'])] # visited_small, can_revisit, path
    while paths:
        visited_small, can_revisit, path = paths.pop()
        v = path[-1]
        for u in d[v]:
            if u == 'end':
                unique_pathes.append(path + [u])
            elif u == 'start':
                pass
            elif u.isupper():
                paths.append((visited_small, can_revisit, path + [u]))
            elif u.islower():
                if u not in visited_small:
                    upd_visited_small = visited_small.copy()
                    upd_visited_small.add(u)
                    paths.append((upd_visited_small, can_revisit, path + [u]))
                elif revisit_allowed and can_revisit:
                    paths.append((visited_small, False, path + [u]))

    return len(unique_pathes)


if __name__ == "__main__":

    convert = lambda lines: [[int(x) for x in line] for line in lines]

    with open('datag/input_12.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    testlines2 = [
        'dc-end',
        'HN-start',
        'start-kj',
        'dc-start',
        'dc-HN',
        'LN-dc',
        'HN-end',
        'kj-sa',
        'kj-HN',
        'kj-dc',
    ]
    testlines3 = [
        'fs-end',
        'he-DX',
        'fs-he',
        'start-DX',
        'pj-DX',
        'end-zg',
        'zg-sl',
        'zg-pj',
        'pj-he',
        'RW-he',
        'fs-DX',
        'pj-RW',
        'zg-RW',
        'start-pj',
        'he-WI',
        'zg-he',
        'pj-fs',
        'start-RW',
    ]
    assert(solve(testlines2) == 19)
    assert(solve(testlines3) == 226)
    assert(solve(testlines2, revisit_allowed=True) == 103)
    assert(solve(testlines3, revisit_allowed=True) == 3509)

    print('p1: ', solve(lines))
    print('p2: ', solve(lines, revisit_allowed=True))
