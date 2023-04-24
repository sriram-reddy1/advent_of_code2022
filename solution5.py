import sys

def print_stacks(crates):
    # print the crate info for debugging
    # the crate number gets placed on top of each array, we can remove it
    for crate in crates:
        for item in crate:
            sys.stdout.write(item)
        print("")

def crate_mover_9000(crates, num_crates, source, dest):
    for i in range(num_crates):
        crates[dest].insert(0, crates[source][0])
        del crates[source][0]

def crate_mover_9001(crates, num_crates, source, dest):
    for i in range(num_crates-1, -1, -1):
        crates[dest].insert(0, crates[source][i])
    for i in range(num_crates):
        del crates[source][0]

if __name__ == '__main__':
    # Read the current crate configuration
    crates = []
    with open("input5.txt", "r") as f:
        # process the crate configuration first
        while True:
            line = f.readline().strip()

            # if we find a blank line, we are done with the crates
            if line == "":
                break

            next_crate = 0
            for i in range(0, len(line), 4):
                if len(crates) < next_crate + 1:
                    crates.append([])
                if i+1 < len(line) and line[i+1] != " ":
                    crates[next_crate].append(line[i+1])
                next_crate += 1

        print_stacks(crates)
        # read the moves and process them
        while True:
            line = f.readline().strip()
            if not line:
                break
            instructions = line.split(" ")
            # format is:
            # move X from N to M
            # here X is the number of items to move
            # N is the origin stack
            # M is the destination stack
            x = int(instructions[1])
            source = int(instructions[3]) - 1
            dest = int(instructions[5]) - 1

            # Part 1
            # crate_mover_9000(crates, x, source, dest)

            # Part 2
            crate_mover_9001(crates, x, source, dest)

        print("crates after rearranging")
        print_stacks(crates)
