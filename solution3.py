import string

def prioritize_letter(letter):
    if letter.islower():
        return ord(letter) - ord('a') + 1
    elif letter.isupper():
        return ord(letter) - ord('A') + 27
    else:
        return -1  # not a letter

def main():
    with open("input3.txt", "r") as file:
        sum_of_priorities = 0
        for line in file:
            size = len(line)
            part1 = line[:size // 2]
            part2 = line[size // 2:]
            common_items = set(part1) & set(part2)
            for item in common_items:
                sum_of_priorities += prioritize_letter(item)
        print(sum_of_priorities)

if __name__ == "__main__":
    main()