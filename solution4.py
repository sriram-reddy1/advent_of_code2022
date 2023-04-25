import os

count = 0
try:
    with open("input4.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            n = line.strip()  # remove newline character at the end
            pair = n.split(",")
            start1 = int(pair[0].split("-")[0])
            end1 = int(pair[0].split("-")[1])
            start2 = int(pair[1].split("-")[0])
            end2 = int(pair[1].split("-")[1])

            # Check if one range fully contains the other
            if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
                count += 1
    print(count)
except IOError as e:
    print("Error reading file:", e)