def sack():
    currentScore = 0
    count = 0
    group = []
    with open("adventOfCode_2022_Day3_Input.txt", "r") as file:
        while True:
            line = file.readline().strip()
            if line and line != "\n":
                # compartmentOne = slice(0, len(line)//2)
                # compartmentTwo = slice(len(line)//2, len(line))
                # shared = "".join(
                #     set(line[compartmentOne]).intersection(line[compartmentTwo]))
                # currentScore += calculateWeight(shared)
                group.append(line)
                count += 1
            if not line:
                break
            if count == 3:
                shared = "".join(
                    set(group[0]).intersection(group[1]).intersection(group[2]))
                group = []
                count = 0
                print(shared)
                currentScore += calculateWeight(shared)

    print("Total Score")
    print(currentScore)


def calculateWeight(character):
    values = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    weights = ['0']
    for x in list(values):
        weights.append(x)
    return weights.index(character)


sack()
