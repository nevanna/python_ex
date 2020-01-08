
from __future__ import unicode_literals

def to_list(str_, lst):
    #teams: {
    #    "team":
    #}

    if lst.get(str_[0]) == None:
        lst[str_[0]] = {"games":0, "win": 0, "draw": 0, "loses":0, "scores" : 0}
    if lst.get(str_[2]) == None:
        lst[str_[2]] = {"games":0, "win": 0, "draw": 0, "loses":0, "scores" : 0}
    if int(str_[1]) > int(str_[3]):
        lst[str_[0]]["win"]+=1
        lst[str_[2]]["loses"]+=1
    elif int(str_[1]) < int(str_[3]):
        lst[str_[2]]["win"]+=1
        lst[str_[0]]["loses"]+=1
    else:
        lst[str_[0]]["draw"]+=1
        lst[str_[2]]["draw"]+=1
    lst[str_[0]]['games']+=1
    lst[str_[2]]['games']+=1
    
def count_scores(lst):
    win_k = 3
    draw_k = 1
    for team in lst:
        lst[team]['scores'] = lst[team]['win'] * win_k + lst[team]['draw'] * 1

def _print_table(lst):
    for team in lst:
        raw = str(team)+":"+ str(lst[team]['games'])+" "+ str(lst[team]['win'])+" "+ str(lst[team]['draw'])+" " + str(lst[team]['loses'])+" "+ str(lst[team]['scores'])
        print(raw)
    

def ma():
    nb = int(input())
    i = 0
    lst = {}
    while i < nb:
        str_ = input()
        str_ = str_.split(';')
        to_list(str_, lst)
        i += 1
    count_scores(lst)
    _print_table(lst)

if __name__ == "__main__":
    ma()
    pass