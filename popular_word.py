def calculate_words(_str, l):
    _str = _str.lower().split(" ")
    for el in _str:
        if l.get(el) == None:
            l[el] = 1
        else:
            l[el] += 1

def compare_raws(l, _max):
    min_raw = _max
    for el in l:
        if l[el] == l[_max]:
            if el < min_raw:
                min_raw = el
    return min_raw

def most_popular(l):
    _max = None
    for el in l:
        if _max == None:
            _max = el
        elif l[_max] < l[el]:
            _max = el
        elif l[_max] == l[el]:
            _max = compare_raws(l, _max)
    return _max

def _main():
    file_name = input()
    l = {} 
    with open(file_name, 'r') as fd:
        while True:
            raw = fd.readline().strip()
            if not raw:
                break
            calculate_words(raw, l)
    key = most_popular(l)
    print(key, l[key])
            


if __name__ == "__main__":
    _main()
    pass