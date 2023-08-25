
class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.data = {}
    
    def writeToFile(self):
        pass

    def loadFromFile(self):
        pass

    def cryptoWriteToFile(self):
        pass

    def cryptoLoadFromFile(self):
        pass

#enc = intEncrypt(strToOrdLst("Hello"), strToOrdLst("key"), 12)
#printInt(enc)
#dec = intDecrypt(enc, strToOrdLst("key"), 12)
#printInt(dec)