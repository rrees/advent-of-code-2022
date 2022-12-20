from dataclasses import dataclass
from day3data import test_data, problem_data

@dataclass
class Backpack:
	slot1: str
	slot2: str

def read_data(data):
	return [s.strip() for s in data.split("\n")]

test_lines = read_data(test_data)

assert len(test_lines) == 6

def make_backpack_from(line):
	assert len(line) % 2 == 0

	mid_point = int(len(line) / 2)

	return Backpack(line[0:mid_point], line[mid_point:])

def create_backpacks(lines):
	return [make_backpack_from(l) for l in lines]

backpacks = create_backpacks(read_data(test_data))

assert len(backpacks) == 6

for backpack in backpacks:
	assert len(backpack.slot1) == len(backpack.slot2)

def duplicate_items(backpack):
	return [
		item
		for item
		in backpack.slot1
		if item in backpack.slot2
	]

def calculate_priority(item):
	return 1 + ord(item[0]) - ord('a')	

def assign_priorities(items):
	return [calculate_priority(item) for item in items]

assert duplicate_items(backpacks[0]) == ['p']

test_priority = assign_priorities(duplicate_items(backpacks[0]))

assert test_priority == [16], f"Actual value was {test_priority}"