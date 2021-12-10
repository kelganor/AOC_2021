# aoc 2021-10


def solve(lines):
    openings = '([{<'
    pair = {'(': ')', '[': ']', '{': '}', '<': '>', }
    miscast = []
    for line in lines:
        stack = []
        for x in line:
            if x in openings:
                stack.append(x)
            else:
                if x == pair[stack[-1]]:
                    stack.pop()
                else:
                    miscast.append(x)
                    break
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = sum([points[x] for x in miscast])

    return(score)


def solve2(lines):
    openings = '([{<'
    pair = {'(': ')', '[': ']', '{': '}', '<': '>', }
    to_complete = []
    for line in lines:
        stack = []
        for x in line:
            if x in openings:
                stack.append(x)
            else:
                if x == pair[stack[-1]]:
                    stack.pop()
                else:
                    stack = []
                    break
        if stack:
            to_complete.append(stack)
    points = {'(': 1, '[': 2, '{': 3, '<': 4}
    scores = []
    for seq in to_complete:
        score = 0
        for x in reversed(seq):
            score = score * 5 + points[x]
        scores.append(score)

    return sorted(scores)[len(scores) // 2]


if __name__ == "__main__":

    with open('data/input_10.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    testlines = [
        '[({(<(())[]>[[{[]{<()<>>',
        '[(()[<>])]({[<{<<[]>>(',
        '{([(<{}[<>[]}>{[]{[(<()>',
        '(((({<>}<{<{<>}{[]{[]{}',
        '[[<[([]))<([[{}[[()]]]',
        '[{[{({}]{}}([{[{{{}}([]',
        '{<[[]]>}<{[{[{[]{()[[[]',
        '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{',
        '<{([{{}}[<[[[<>{}]]]>[]]',
    ]
    assert(solve(testlines) == 26397)
    assert(solve2(testlines) == 288957)

    print('p1: ', solve(lines))
    print('p2: ', solve2(lines))
