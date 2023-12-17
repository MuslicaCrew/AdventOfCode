import sys

with open(sys.argv[1], "r") as file:
    answer = 0
    rMax = 12
    gMax = 13
    bMax = 14
    for line in file:
        reds = []
        greens = []
        blues = []
        id = int(line.split(":")[0][-2:])
        games = str(line.split(":")[1]).split("; ")
        for pulls in games:
            balls = pulls.split(", ")
            for ball in balls:
                ball = str(ball).strip()
                color = str(ball[2:]).strip()
                number = str(ball).strip()[0:2]
                if color == "blue":
                    blues.append(int(number))
                if color == "red":
                    reds.append(int(number))
                if color== "green":
                    greens.append(int(number))
        # For part one uncomment the line below and do proper indentation
        #if max(reds) <= rMax and max(greens) <= gMax and max(blues) <= bMax:
        answer += max(reds) * max(greens) * max(blues)
    print(answer)
