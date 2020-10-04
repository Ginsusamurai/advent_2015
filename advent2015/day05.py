import csv
import re

if __name__ == "__main__":
    with open("inputs/day05input.csv", newline='') as f:
        reader = csv.reader(f)
        stringList = list(reader)

    niceStrings = set()
    print(stringList)

    # stringList = [['ugknbfddgicrmopn']]

    for string in stringList:

        print(bool(re.search(r"[aeiou].*[aeiou].*[aeiou]", string[0])))
        print(bool(re.search(r"(.)\1", string[0])))
        print(bool(re.search("(ab|cd|pq|xy)", string[0])))

        if re.search(r"[aeiou].*[aeiou].*[aeiou]", string[0]) \
                and re.search(r"(.)\1", string[0]) \
                and not re.search("(ab|cd|pq|xy)", string[0]):
            niceStrings.add(string[0])

    print("Day05.1 -> There are {} nice strings.".format(len(niceStrings)))
