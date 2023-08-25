def isExist(path):
    try:
        open(path)
    except IOError as e:
        return False
    else:
        return True

def readFileLine(name, ind):
    with open(name, encoding="utf-8") as f:
        return f.read().splitlines()[ind]

def readFileLines(name):
    with open(name, encoding="utf-8") as f:
        return f.read().splitlines()

def addToFile(name, line, end=''):
    with open(name, "a", encoding="utf-8") as f:
        f.write(line + end)

def clearFile(name):
    with open(name, "w", encoding="utf-8") as f:
        f.write("")

def writeToFile(name, text, end=''):
    with open(name, "w+", encoding="utf-8") as f:
        f.write(text + end)

def createFile(path):
    writeToFile(path, "")


def lineToDict(path, ind):
    splline = readFileLines(path)[ind].split()
    return {splline[0] : splline[1:]}

def linesToDicts(path):
    x = []
    for i in readFileLines(path):
        x.append({i.split()[0] : i.split()[1:]})
    return x

def isLineInFile(path, line):
    lines = readFileLines(path)
    return line in lines


def getLastLine(name):
    return readFileLines(name)[-1]

def getlJSTRING(req):
    return str(list(req.form.to_dict().items())[0][0])

def getDictFromJSON(jsonstr):
    x = jsonstr.split(":")
    return {x[0][1:-2] : x[1][1:-1]}


def parseDLinesWhile(path, rightKey):
    ldict = linesToDicts(path)
    for i in ldict:
        if(list(i.keys())[0] == rightKey):
            return i
    return 'No such element'