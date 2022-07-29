import requests
from discordBot import discordBot
import fileManager
import ipHelper

alerts = []

fileVal = fileManager.readVal()
dnsVal = None

if fileVal == "":
    dnsVal = ipHelper.getDnsIp()

    if dnsVal == None:
        alerts.append("DynDns: Dns record not found after empty local file")
    else:
        fileVal = dnsVal
        fileManager.saveVal(fileVal)
        alerts.append("DynDns: Dns record file successfully saved")

pubVal = ipHelper.getPubIp()

if pubVal != fileVal:
    urlAdd = ipHelper.getAddUrl(pubVal)
    urlDel = ipHelper.getDelUrl(pubVal)

    dnsVal = ipHelper.getDnsIp()
    
    if dnsVal != None:
        delResp = requests.get(urlDel).json()
        if delResp['result'] != "success":
            alerts.append("DynDns: Failure to delete dns record")

    addResp = requests.get(urlAdd, verify = True).json()

    if addResp['result'] != "success":
        alerts.append("DynDns: Error adding dns record")
    else:
        alerts.append("DynDns: Dns record update: " + addResp['result'] + " - " + addResp['data'] + " for ip " + pubVal)
        fileManager.clearFile()

dscrd = discordBot()
dscrd.sendAlerts(alerts)