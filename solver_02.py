# aoc 2021-02

def solve(lines):
	y, x = 0, 0
	for line in lines:
		command, dr = line.split()
		dr = int(dr)
		if command == 'forward':
			x += dr
		elif command == 'up':
			y -= dr
		elif command == 'down':
			y += dr
	return y * x


def solve2(lines):
	y, x, aim = 0, 0, 0
	for line in lines:
		command, dr = line.split()
		dr = int(dr)
		if command == 'forward':
			x += dr
			y += dr * aim
		elif command == 'up':
			aim -= dr
		elif command == 'down':
			aim += dr
	return y * x


if __name__ == "__main__":

	with open('input_02.txt') as f:
		lines = f.readlines()

	print(solve(lines))
	print(solve2(lines))