# Alphabet in english
alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

actualFileStr = ""
responseStr = ""
selection = ""
inputFilename = ""
inputKey = ""

lines = []

isCorrectInput = False
isCorrectKey = False
isCoded = False

indexKey = 0

def openFile(filename):
    global actualFileStr
    file = open(filename,"r")
    actualFileStr = file.read().lower()
    file.close()

def writeFile(filename):
    file = open(filename,"w")
    file.writelines("%s" % i for i in lines)
    file.close()

def moduleLetter(letter):
    indexWordAlpha = 0
    if "code" == selection.lower():
        indexWordAlpha = (alphabet[letter] + indexKey) % 26
    else:
        indexWordAlpha = (alphabet[letter] - indexKey) % 26
    return list(alphabet.items())[indexWordAlpha][0]

def handleSelection():
    global decodedWord, indexKey
    openFile(inputFilename)

    rangeValue = 1 if isCoded else 26

    for x in range(rangeValue):
        decodedWord = ''
        indexKey = inputKey if isCoded else x 
        for ltr in actualFileStr:
            if ltr.isalpha():
                decodedWord += moduleLetter(ltr)
            else:
                decodedWord += ltr
        lines.append("\n----- Key: " + str(indexKey) + " ------\n")
        lines.append(decodedWord)

def checkInput(str):
    global isCorrectInput, isCoded
    if str.lower() == "code" or str.lower() == "decoded":
        isCoded = True if "code" == str.lower() else False
        isCorrectInput = True
    else:
        isCorrectInput = False
        print("Incorrect input\n")

def checkNumber(num):
    global inputKey, isCorrectKey
    if num.isnumeric():
        inputKey = int(num)
        isCorrectKey = True
    else:
        isCorrectKey = False
        print("Invalid Key\n")

def getInputUser():
    global selection, inputFilename
    while not isCorrectInput:
        print("¿Code or decoded?:")
        selection  = input()
        checkInput(selection)
    if "code" == selection.lower():
        while not isCorrectKey:
            print("Enter keycode:")
            checkNumber(input())
    print("filename?:")
    inputFilename = input()


def main():
    getInputUser()
    handleSelection()
    writeFile("res.txt")

main()



