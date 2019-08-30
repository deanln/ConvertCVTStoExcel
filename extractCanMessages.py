

class logEntry:
    def __init__(self, flushCount=None, faultSymbol=None, msg3=None, msg4=None, msg7=None):
        self.flushCount = flushCount
        self.faultSymbol = faultSymbol
        self.msg3 = msg3
        self.msg4 = msg4
        self.msg7 = msg7

    def setFlushCount(self, flushCount):
        self.flushCount = flushCount
    def getFlushCount(self):
        return self.flushCount

    def setFaultSymbol(self, faultSymbol):
        self.faultSymbol = faultSymbol
    def getFaultSymbol(self):
        return self.faultSymbol

    def setMsg3(self, msg3):
        self.msg3 = msg3
    def getMsg3(self):
        return self.msg3

    def setMsg4(self, msg4):
        self.msg4 = msg4
    def getMsg4(self):
        return self.msg4

    def setMsg7(self, msg7):
        self.msg7 = msg7
    def getMsg7(self):
        return self.msg7

    def printToString(self):
        print(self.flushCount[0] + ": " + self.flushCount[1])
        print(self.faultSymbol[0] + ": " + self.faultSymbol[1])
        print(self.msg3[0] + ": " + self.msg3[1])
        print(self.msg4[0] + ": " + self.msg4[1])
        print(self.msg7[0] + ": " + self.msg7[1])

    
def createDataList(fileName):
    """
    Reads in data from log file line by line and converts it into a list
    of logEntry objects.
    """
    listOfEntries = []
    with open(fileName,"r") as file:
        entryToAppend = None
        for line in file.readlines():
            if line.find("FLUSH_CNT") != -1:
                entryToAppend = logEntry(None, None, None, None, None)
                entryToAppend.setFlushCount(dataToTuple(line))
            elif line.find("FLT_SYMBOL") != -1:
                entryToAppend.setFaultSymbol(dataToTuple(line))
            elif line.find("CM_003MSG") != -1:
                cleanedLine = line.replace("MSG","")
                entryToAppend.setMsg3(dataToTuple(cleanedLine))
            elif line.find("CM_004MSG") != -1:
                cleanedLine = line.replace("MSG","")
                entryToAppend.setMsg4(dataToTuple(cleanedLine))
            elif line.find("CM_007MSG") != -1:
                cleanedLine = line.replace("MSG","")
                entryToAppend.setMsg7(dataToTuple(cleanedLine))
                listOfEntries.append(entryToAppend)
    return listOfEntries


def dataToTuple(stringData):
    """
    Formats string to tuple ("id:data" -> (id,data))
    """
    splitLine = stringData.split(": ")
    result = (splitLine[0],splitLine[1].strip("\n"))
    return result


def run(fileName):
    dataList = createDataList(fileName)
    for entry in dataList:
        entry.printToString()

if __name__ == '__main__':
    pass
    #run(r"C:\Users\tyler.vu\Desktop\Stuff\Python\dean\F9LX-300 CVTS NVM dnld 25OCT2018.txt")
    
