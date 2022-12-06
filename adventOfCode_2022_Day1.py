
def count():
    values = []
    current = 0
    with open("adventOfCode_2022_Day1_Input.txt", "r") as file:
        while True:
            line = file.readline()
            if line and line != "\n":
                current += int(line)
            else:
                values.append(current)
                current = 0
            if not line:
                break
    values.sort(reverse=True)
    print("Total Calories")
    print(values[0])
    print()
    print("Top 3")
    top3 = slice(3)
    print(', '.join(map(str, values[top3])))
    print("Total Calories in Top 3")
    print(sum(values[top3]))


count()
