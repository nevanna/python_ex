
def create_decod_lst(lst, original, sipher):
    i = 0
    while i < len(original):
        if lst.get(original[i]) == None:
            lst[original[i]] = sipher[i] 
        i+=1

def code(str_, lst):
    new_str = ""
    for liter in str_:
        new_str += lst[liter]
    return new_str

def decode(str_, lst):
    new_str = ""
    for liter in str_:
        for zn in lst:
            if lst[zn] == liter:
                new_str += zn
                break
    return new_str

def sipher():
    original = str(input())
    sipher = str(input())
    third = str(input())
    forth = str(input())
    lst = {}
    create_decod_lst(lst, original, sipher)
    print(code(third, lst))
    print(decode(forth, lst))
if __name__ == "__main__":
    sipher()
    pass