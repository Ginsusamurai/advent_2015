import csv
from day01 import splitter




if __name__ == "__main__":
    with open("inputs/day03input.csv", newline='') as f:
        reader = csv.reader(f)
        packages = splitter(list(reader)[0][0])

    print(len(packages))

    gifted = [[0,0]]
    pos = [0,0]

    for step in packages:
        # print(step)
        if step == "<":
            pos[0] -= 1
        elif step == ">":
            pos[0] += 1
        elif step == "^":
            pos[1] += 1
        elif step == "V":
            pos[1] -= 1

        if pos not in gifted:
            gifted.append(pos[:])

    print(gifted)