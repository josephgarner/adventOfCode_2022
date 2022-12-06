# JDTMRWCQJ Not right


def pairs():
    state = [['F', 'H', 'B', 'V', 'R', 'Q', 'D', 'P'],
             ['L', 'D', 'Z', 'Q', 'W', 'V'],
             ['H', 'L', 'Z', 'Q', 'G', 'R', 'P', 'C'],
             ['R', 'D', 'H', 'F', 'J', 'V', 'B'],
             ['Z', 'W', 'L', 'C'],
             ['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'],
             ['J', 'R', 'L', 'V', 'M', 'B', 'S'],
             ['D', 'P', 'J'],
             ['D', 'C', 'N', 'N', 'W', 'V']]
    topCrates = ""
    with open("adventOfCode_2022_Day5_Input.txt", "r") as file:
        while True:
            line = file.readline().strip()
            if line and line != "\n":
                data = [int(s) for s in line.split() if s.isdigit()]
                print(line)
                print(data)
                step = 0
                crane = []
                while step < data[0]:
                    # amount start finish
                    block = state[data[1] - 1].pop()
                    crane.insert(0, block)
                    step += 1
                for tempBlock in crane:
                    state[data[2]-1].append(tempBlock)
            if not line:
                break
    for stack in state:
        if (len(stack)):
            topCrates += stack[len(stack)-1]
    print("Answer")
    print(topCrates)


pairs()
