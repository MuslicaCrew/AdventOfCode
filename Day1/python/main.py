import sys

values = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
answer = 0

with open(sys.argv[1], "r") as file:
    for line in file:
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(int(c))
            for j, value in enumerate(values):
                if line[i:].startswith(value):
                    digits.append(j+1)
        answer += digits[0] * 10 + digits[-1]
    print("Answer: ", answer)
