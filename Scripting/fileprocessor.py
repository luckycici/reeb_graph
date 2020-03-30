import sys

def loadWRL(fileName):
    with open(fileName) as fp:
        return fp.read()

def processLines(line, seperator):
    newLine = ""
    str = line.split()
    count = 0
    for s in str:
        newLine += s
        count += 1        
        if count % seperator == 0:
            newLine += ",\n"
        else:
            newLine += " "
    return newLine

def listToString(s): 
    str1 = " "  
    return (str1.join(s)) 

def processWRL():
    text = loadWRL(sys.argv[1])
    lines = text.split("\n")
    coordList = []
    for l in lines:
        nl = ""
        if l.find("point") != -1:
            nl = processLines(l, 3)
        elif l.find("coordIndex") != -1:
            nl = processLines(l, 4)
        else:
            nl = l
        nl += "\n"
        coordList.append(nl)
    return coordList

def saveWRL():
    fileList = processWRL()
    fileStr = listToString(fileList)    
    text_file = open("test.wrl", "w")
    text_file.write(fileStr)
    text_file.close()
    
saveWRL()
