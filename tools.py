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

def addToFile(name, line, end='\n'):
    with open(name, "a", encoding="utf-8") as f:
        f.write(line + end)

def clearFile(name):
    with open(name, "w", encoding="utf-8") as f:
        f.write("")

def writeToFile(name, text, end=''):
    with open(name, "w+", encoding="utf-8") as f:
        f.write(text + end)

def delFromFile(path, line):
    lines = readFileLines(path)
    nlines = []
    for l in lines:
        if l != line:
            nlines.append(l)
    writeToFile(path, "\n".join(nlines))

def createFile(path):
    writeToFile(path, "")


def lineToDict(path, ind):
    splline = readFileLines(path)[ind].split()
    return {splline[0] : splline[1:]}

def linesToDicts(path, splch = ' '):
    x = []
    for i in readFileLines(path):
        x.append({i.split(splch)[0] : "".join(i.split(splch)[1:])})
    return x

def isLineInFile(path, line):
    lines = readFileLines(path)
    return line in lines


def getLastLine(name):
    return readFileLines(name)[-1]

def getlJSTRING(req):
    return str(list(req.form.to_dict().items())[0][0])

def getDictFromJSON(jsonstr):
    
    outDict = {}

    x = jsonstr.split(",")[:-1]
    for el in x:
        outDict[el.split(":")[0].replace('"', '')] = el.split(":")[1].replace('"', '')

    return outDict


def parseDLinesWhile(path, rightKey, splch = ' ', inv = False):
    ldict = linesToDicts(path, splch)
    for i in reversed(ldict):
        if(not inv and list(i.keys())[0] == rightKey):
            return i
        elif inv and list(i.keys())[0] != rightKey:
            return i
    return 'No such element'

def convertFromWstring(wstring):
    return "".join([chr(int(i)) for i in wstring.split()])

def convertToWstring(string):
    return " ".join([str(ord(i)) for i in string])