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
        alerts.append("DynDns: Dns record file successfully saved")
        fileVal = dnsVal
        fileManager.saveVal(fileVal)

pubVal = ipHelper.getPubIp()

if pubVal != fileVal:
    urlAdd = "https://api.dreamhost.com/?key={key}&format={format}&cmd={cmd}&type={type}&record={record}&value={value}".format(key=key, format=frmt, cmd=cmdAdd, type=recordType, record=record, value=pubVal)
    urlDel = "https://api.dreamhost.com/?key={key}&format={format}&cmd={cmd}&type={type}&record={record}&value={value}".format(key=key, format=frmt, cmd=cmdDel, type=recordType, record=record, value=pubVal)

    dnsVal = ipHelper.getDnsIp()
    
    if dnsVal != None:
        delResp = requests.get(urlDel).json()
        if delResp['result'] != "success":
            alerts.append("DynDns: Failure to delete dns record")

    addResp = requests.get(urlAdd, verify = True).json()

    if addResp['result'] != "success":
        alerts.append("DynDns: Error adding dns record")
    else:
        alerts.append("DynDns: Dns record update: " + addResp['result'] + " - " + addResp['data'] + " to ip " + pubVal)
        fileManager.clearFile()

dscrd = discordBot()
dscrd.sendAlerts(alerts)