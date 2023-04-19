import os

win = 6
tie = 3
lose = 0

rock = 1
paper = 2
scissors = 3

def getScorePart1(line):
    results = {
        "A Y": win + paper,  # A - rock, Y - paper
        "A X": tie + rock,   #           X - Rock
        "A Z": lose + scissors,  #          Z - scissors
        "B Y": tie + paper,  # B - paper
        "B X": lose + rock,
        "B Z": win + scissors,
        "C Y": lose + paper, # C - scissors
        "C X": win + rock,
        "C Z": tie + scissors
    }
    return results[line]

def getScorePart2(value):
    results = {
        "A Y": tie + rock,  # A - rock
        "A X": lose + scissors,  #           X - Rock
        "A Z": win + paper, #          Z - scissors
        "B Y": tie + paper,  # B - paper
        "B X": lose + rock,
        "B Z": win + scissors,
        "C Y": tie + scissors, # C - scissors
        "C X": lose + paper,
        "C Z": win + rock
    }
    return results[value]

totalScore1 = 0
totalScore2 = 0

try:
    with open("input2.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            scorePart1 = getScorePart1(line.strip())
            scorePart2 = getScorePart2(line.strip())
            totalScore1 += scorePart1
            totalScore2 += scorePart2
except IOError as e:
    print(e)

print("Part 1 score is", totalScore1)
print("Part 2 score is", totalScore2)
