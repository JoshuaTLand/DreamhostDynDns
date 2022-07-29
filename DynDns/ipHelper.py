import requests

key = "YOURKEY"
cmdAdd = "dns-add_record"
cmdDel = "dns-remove_record"
cmdGet = "dns-list_records"
recordType = "A"
frmt = "json"
record = "example.com"

def getPubIp():
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify = True)

    if response.status_code != 200:
        return None

    data = response.json()

    return data['ip']

def getDnsIp():
    urlGet = "https://api.dreamhost.com/?key={key}&format={format}&cmd={cmd}&type={type}&record={record}".format(key=key, format=frmt, cmd=cmdGet, type=recordType, record=record)
    dnsRecords = requests.get(urlGet, verify=True).json()

    for dnsRecord in dnsRecords['data']:
        if dnsRecord['record'] == record:
            return dnsRecord['value']

    return None

def getAddUrl(pubVal):
    return "https://api.dreamhost.com/?key={key}&format={format}&cmd={cmd}&type={type}&record={record}&value={value}".format(key=key, format=frmt, cmd=cmdAdd, type=recordType, record=record, value=pubVal)

def getDelUrl(pubVal):
    return "https://api.dreamhost.com/?key={key}&format={format}&cmd={cmd}&type={type}&record={record}&value={value}".format(key=key, format=frmt, cmd=cmdDel, type=recordType, record=record, value=pubVal)
