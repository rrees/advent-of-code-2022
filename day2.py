from dataclasses import dataclass

from day2data import guide

def read_data(data):
    lines = data.split("\n")
    return [line.split(" ") for line in lines]

@dataclass
class ThrowData:
    score: int
    beats: str
    matches: str

lookup = {
    'X': ThrowData(1, 'C', 'A'),
    'Y': ThrowData(2, 'A', 'B'),
    'Z': ThrowData(3, 'B', 'C')
}
scores = {
    'X' : 1,
    'Y': 2,
    'Z': 3,
}

wins = {
    'X' : 'C',
    'Y': 'A',
    'Z': 'B',
}

matches = {
    'X' : 'A',
    'Y': 'B',
    'Z': 'C',
}

def score_throw(their_throw, my_throw):
    if their_throw == matches[my_throw]:
        return scores[my_throw] + 3
    
    if wins[my_throw] == their_throw:
        return scores[my_throw] + 6
    
    return scores[my_throw]

def score_throw2(their_throw, my_throw):
    play_data = lookup[my_throw]

    if play_data.beats == their_throw:
        return play_data.score + 6
    
    if play_data.matches == their_throw:
        return play_data.score + 3

    return play_data.score

def calculate_score(data):
    total_score = 0

    for throws in read_data(data):
        total_score += score_throw2(throws[0], throws[1])

    return total_score

print(calculate_score(guide))

test_data = """A Y
B X
C Z"""

test_score = calculate_score(test_data)
assert test_score == 15, f"Calculated score was {test_score}"