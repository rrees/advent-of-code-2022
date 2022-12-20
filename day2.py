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
    'Z': ThrowData(3, 'B', 'C'),
    'A': ThrowData(1, 'C', 'A'),
    'B': ThrowData(2, 'A', 'B'),
    'C': ThrowData(3, 'B', 'C'),
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
    play_data = lookup[my_throw]

    if play_data.beats == their_throw:
        return play_data.score + 6
    
    if play_data.matches == their_throw:
        return play_data.score + 3

    return play_data.score

def calculate_score(data):
    total_score = 0

    for throws in read_data(data):
        total_score += score_throw(throws[0], throws[1])

    return total_score


# A Rock, B Paper, C Scissors
appropriate_response = {
    'XA': 'C',
    'ZA': 'B',
    'XB': 'A',
    'ZB': 'C',
    'XC': 'B',
    'ZC': 'A',
}

def calculate_score2(data):
    def determine_throw(their_throw, outcome):

        if outcome == 'Y':
            return their_throw

        return appropriate_response[outcome + their_throw]
    total_score = 0

    for throws in read_data(data):
        total_score += score_throw(throws[0], determine_throw(throws[0], throws[1]))

    return total_score

test_data = """A Y
B X
C Z"""

test_score = calculate_score(test_data)
test_score_2 = calculate_score2(test_data)

for score, expected_score in ((test_score, 15), (test_score_2, 12)):
    assert score == expected_score, f"Calculated score was {score}"
 
print(calculate_score(guide), calculate_score2(guide))
