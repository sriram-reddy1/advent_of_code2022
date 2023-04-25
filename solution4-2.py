import os

count = 0

try:
    with open("input4-2.txt", 'r') as file:
        for line in file:
            pair = line.strip().split(',')
            start1 = int(pair[0].split('-')[0])
            end1 = int(pair[0].split('-')[1])
            start2 = int(pair[1].split('-')[0])
            end2 = int(pair[1].split('-')[1])

            # Check if one range fully contains the other
            if end1 >= start2 and end2 >= start1:
                count += 1

    print(count)

except IOError as e:
    print("Error reading file:", e)