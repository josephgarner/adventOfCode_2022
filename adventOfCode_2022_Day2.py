
"""
Player 1
1       2       3
A Rock, B Paper, C Scissors

Player 2
1       2       3
X Rock, Y Paper, Z Scissors

AA = 3
AB = 6
AC = 0

BA = 0
BB = 3
BC = 6

CA = 6
CB = 0
CC = 3

"""

# 9816


def game():
    cost = {"A": 1, "B": 2, "C": 3}
    # results = dict({"A X": 3, "A Y": 6, "A Z": 0, "B X": 0,
    #                 "B Y": 3, "B Z": 6, "C X": 6, "C Y": 0, "C Z": 3})
    results = dict({"X": 0, "Y": 3, "Z": 6})
    currentScore = 0
    with open("adventOfCode_2022_Day2_Input.txt", "r") as file:
        while True:
            line = file.readline()
            if line and line != "\n":
                moves = line.split()
                currentScore += results.get(moves[1])

                currentScore += cost.get(calculateMove(moves[1], moves[0]))
            if not line:
                break
    print("Total Score")
    print(currentScore)


def calculateMove(rule, move):
    if rule == "X" and move == "A":
        return "C"
    elif rule == "X" and move == "B":
        return "A"
    elif rule == "X" and move == "C":
        return "B"
    elif rule == "Z" and move == "A":
        return "B"
    elif rule == "Z" and move == "B":
        return "C"
    elif rule == "Z" and move == "C":
        return "A"
    return move


game()
