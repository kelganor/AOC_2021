# aoc 2021-04


def map_nums_to_boards(boards):

    num2boards = {}
    for i, b in enumerate(boards):
        for y, line in enumerate(b):
            for x, el in enumerate(line):
                if el in num2boards:
                    num2boards[el].append((i, y, x))
                else:
                    num2boards[el] = [(i, y, x)]

    return num2boards


def calculate_score(boards, order, winner, stop):

    win_b = set()
    for line in boards[winner]:
        win_b.update(line)
    res = (sum(win_b) - sum([el for el in order[:stop+1] if el in win_b])) * order[stop]

    return res


def solve(order, boards):

    num2boards = map_nums_to_boards(boards)
    rows_bingo = {}
    cols_bingo = {}
    winner = -1
    stop = -1
    for k, el in enumerate(order):
        for i, y, x in num2boards[el]:
            rows_bingo[(i, y)] = rows_bingo.get((i, y), 0) + 1
            cols_bingo[(i, x)] = cols_bingo.get((i, x), 0) + 1
            if cols_bingo[(i, x)] == 5 or rows_bingo[(i, y)] == 5:
                winner = i
                stop = k
                break
        if winner > 0:
            break

    return calculate_score(boards, order, winner, stop)


def solve2(order, boards):

    num2boards = map_nums_to_boards(boards)
    won = set()
    rows_bingo = {}
    cols_bingo = {}
    winner = -1
    stop = -1
    for k, el in enumerate(order):
        for i, y, x in num2boards[el]:
            rows_bingo[(i, y)] = rows_bingo.get((i, y), 0) + 1
            cols_bingo[(i, x)] = cols_bingo.get((i, x), 0) + 1
            if (cols_bingo[(i, x)] == 5 or rows_bingo[(i, y)] == 5) and i not in won:
                won.add(i)
                winner = i
                stop = k

    return calculate_score(boards, order, winner, stop)


if __name__ == "__main__":

    with open('data/input_04.txt') as f:
        lines = [x.strip() for x in f.readlines()]
    order = list(map(int, lines[0].split(',')))

    boards = []
    for i, line in enumerate(lines[1:]):
        if i % 6 == 0:
            board = []
            continue
        board.append(
            list(map(int, line.split()))
        )
        if len(board) == 5:
            boards.append(board)

    print('p1: ', solve(order, boards))
    print('p2: ', solve2(order, boards))