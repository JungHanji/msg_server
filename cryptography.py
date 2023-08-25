def listToStr(lst): return " ".join(lst)

def intEncrypt(string, key, altKey):
    if(len(key) > len(string)): key = [key[x] for x in range(0, len(key), len(key)//len(string))]
    return [string[i] * key[i%len(key)] * altKey for i in range(len(string))]

def intDecrypt(string, key, altKey):
    return [string[i] // altKey // key[i%len(key)] for i in range(len(string))]

def hexify(lst):
    return ["".join([str(hex(i))[2:] for i in lst]), len(str(hex(lst[0]))[2:])]

def unHexify(string, hexLen):
    return [int(string[i:i+hexLen], 16) for i in range(0, len(string), hexLen)]

def strEncrypt(string, key, altKey):
    return hexify(intEncrypt(strToOrdLst(string), strToOrdLst(key), altKey))

def strDecrypt(string, key, altKey, hexKey):
    x = unHexify(string,hexKey)
    y = intDecrypt(x, key, altKey)
    return "".join([chr(y[i]) for i in range(len(y))])


def printInt(lst):
    for i in lst:
        try:
            print(chr(i),end='')
        except:
            print(f" ERROR:{i} ", end='')
    print()

def strToOrdLst(string): return [ord(i) for i in string]