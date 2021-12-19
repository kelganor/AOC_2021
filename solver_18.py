# aoc 2021-18


import json


def flattern(fseq, d=0):
    if type(fseq) == int:
        return [[fseq, d]]
    else:
        return flattern(fseq[0], d=d+1) + flattern(fseq[1], d=d+1)


def explode(fseq, d=5):
    L = len(fseq)
    for i, j in zip(range(L-1), range(1, L)):
        (xi, di), (xj, dj) = fseq[i], fseq[j]
        if di == dj == 5:
            if i > 0:
                fseq[i-1][0] += xi
            if j < L-1:
                fseq[j+1][0] += xj
            fseq[i] = [0, di-1]
            fseq = [el for k, el in enumerate(fseq) if k != j]
            return True, fseq

    return False, fseq


def split(fseq):
    for i in range(len(fseq)):
        xi, di = fseq[i]
        if xi >= 10:
            fseq = fseq[:i] + [
                [xi//2, di+1], [xi - xi//2, di+1]
            ] + fseq[i+1:]
            return True, fseq
    return False, fseq


def seq_reduce(fseq):
    while True:
        done, fseq = explode(fseq)
        if done: continue
        done, fseq = split(fseq)
        if done: continue
        break
    return fseq


def magnitude(fseq, dmax=4):
    for d in range(dmax, 0, -1):
        i = 0
        while i < len(fseq) - 1:
            (xi, di), (xj, dj) = fseq[i], fseq[i+1]
            if di == dj == d:
                fseq = fseq[:i] + [[ 3* xi + 2 * xj, d-1]] + fseq[i+2:]
            i += 1
    return fseq[0][0]


def solve(lines):
    cur = flattern(json.loads(lines[0]))
    for x in lines[1:]:
        xseq = flattern(json.loads(x))
        cur = seq_reduce([[x, d+1] for x, d in cur+xseq])
    return magnitude(cur)


def solve2(lines):
    L = len(lines)
    res = 0
    for i in range(L):
        for j in range(L):
            if i == j: continue
            a = flattern(json.loads(lines[i]))
            b = flattern(json.loads(lines[j]))

            res = max(
                res, magnitude(
                    seq_reduce([[x, d+1] for x, d in a+b])
            ))
    return res

if __name__ == "__main__":
    with open('data/input_18.txt') as f:
        lines = f.read().strip().split('\n')

    print('p1::', solve(lines))
    print('p2::', solve2(lines))
