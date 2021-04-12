from random import shuffle

def arrStringLength(arrString):
    return sum([len(x) for x in arrString]) + max(len(arrString) - 1, 0)


def justifyArrString(arrString, target):
    if arrStringLength(arrString) + len(arrString) < target:
        return arrString
    else:
        indexes = list(range(0, len(arrString) - 1))
        shuffle(indexes)
        for i in indexes:
            if arrStringLength(arrString) < target:
                arrString[i] += " "
            else:
                break
        return arrString


def formatText(text, width = 80, justify = False):
    lines = []
    for line in text.split("\n"):
        newLine = []
        for word in line.split(" "):
            newLine.append(word)
        lines.append(newLine)
    rawLines = []
    for line in lines:
        newLine = []
        for word in line:
            if arrStringLength(newLine + [word]) + 1 > width:
                rawLines.append(newLine)
                newLine = [word]
            else:
                newLine.append(word)
        rawLines.append(newLine)
    if justify:
        rawLines = [justifyArrString(x, width) for x in rawLines]
    resultString = ""
    for line in rawLines:
        resultString += " ".join(line) + "\n"
    return resultString.strip()


if __name__ == '__main__':
    import sys
    try:
        targetWidth = int(sys.argv[1])
    except IndexError:
        targetWidth = 80
    print(formatText(sys.stdin.read(), targetWidth, True))


        
