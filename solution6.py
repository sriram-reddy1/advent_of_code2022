import string

def part1(line):
    result = ""
    for i in range(len(line) - 3):
        chars = line[i:i + 4]
        uniqueChars = set(chars)

        if len(uniqueChars) == 4:
            result = chars
            return i+4
    return 0

def part2(line):
    result = ""
    for i in range(len(line) - 13):
        chars = line[i:i + 14]
        uniqueChars = set(chars)

        if len(uniqueChars) == 14:
            result = chars
            return i+14
    return 0

with open("input6.txt", "r") as f:
    for line in f:
        line = line.strip()
        j = part1(line)
        n = part2(line)
        print("part 1 answer is:", j)
        print("part 2 answer is:", n)
