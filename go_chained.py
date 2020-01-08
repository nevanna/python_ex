import requests

file_name = str(input())
first = None
with open(file_name, 'r') as fd:
    first = fd.readline()
adr = 'https://stepic.org/media/attachments/course67/3.6.3/'
i = 0
if first:
    while True:
        r = requests.get(first)
        print(r.text)
        print(i)
        i+=1
        formatting = r.text.splitlines()
        if formatting[0].find('We') == 0:
            with open('rez2.txt', 'w') as fd2:
                print(r.text, file = fd2)
            break
        else:
            first = adr + formatting[0].strip()
