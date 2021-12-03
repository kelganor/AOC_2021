# aoc 2021-01

def solve(nums, w):
	return sum([1 if b > a else 0 for a, b in zip(nums[:-w], nums[w:])])


if __name__ == "__main__":
	
	with open('input_01.txt') as f:
		lines = f.readlines()
	nums = list(map(int, lines))
	
	print(solve(nums, 1))
	print(solve(nums, 3))