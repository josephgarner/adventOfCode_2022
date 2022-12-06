# 491 Wrong Too High

def pairs():
    currentCount = 0
    with open("adventOfCode_2022_Day4_Input.txt", "r") as file:
        while True:
            line = file.readline().strip()
            if line and line != "\n":
                elves = line.split(',')
                print(elves)
                # print(assignmenstOverlaps(elves))
                if assignmenstOverlaps(elves):
                    currentCount += 1
            if not line:
                break

    print("Answer")
    print(currentCount)


def assignmenstOverlaps(pair):
    one = pair[0].split('-')
    two = pair[1].split('-')

    job = int(one[0])
    assignmentOne = []
    while job <= int(one[1]):
        assignmentOne.append(job)
        job += 1

    job = int(two[0])
    assignmentTwo = []
    while job <= int(two[1]):
        assignmentTwo.append(job)
        job += 1

    intersection = list(set(assignmentOne) & set(assignmentTwo))

    return len(intersection) > 0


pairs()
