import requests

file_name = str(input())
adr = None
with open(file_name, 'r') as fd:
    adr = fd.readline()

if adr:
    r = requests.get(adr)
    print(r.text)
    t = r.text.splitlines()
    print("!!!!!!!i")
    print(t)
    _len = len(t)
    print(_len)
