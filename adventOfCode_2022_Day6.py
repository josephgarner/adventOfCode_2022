# 1739 WRONG
# 1738 WRONG
# 1736 WRONG
# 54 WRONG
# 48 WRONG

def getMarker():
    marker = 0
    nonRepeat = ""
    distinct = ""
    with open("adventOfCode_2022_Day6_Input.txt", "r") as file:
        while True:
            line = file.readline().strip()
            char_arr = list(line)
            if line and line != "\n":
                # while len(nonRepeat) < 4:
                #     if char_arr[marker] not in nonRepeat:
                #         nonRepeat += char_arr[marker]
                #         marker += 1

                #     else:
                #         nonRepeat = ""
                # print(nonRepeat)
                while len(set(list(distinct))) < 14:
                    distinct = line[marker: marker + 14]
                    if len(set(list(distinct))) < 14:
                        marker += 1
                    else:
                        marker += 14
                print(distinct)
                print("".join(list(distinct)))
            if not line:
                break

    print("Answer")
    print(marker)


getMarker()
