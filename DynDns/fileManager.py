from os import path

fileName = "dnsIp"

def saveVal(val):
    with open(fileName, 'w+') as f:
        f.truncate()
        f.write(val)

def readVal():
    if not path.isfile(fileName):
        with open(fileName, "w+") as file:
            file.write("")
    with open(fileName, 'r') as f:
        return f.readline()

def clearFile():
    with open(fileName, "w+") as file:
        file.truncate()
        file.write("")