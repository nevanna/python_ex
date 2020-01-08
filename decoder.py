def rd():
    file_name = input()
    _str = ""
    with open(file_name, 'r') as fd:
       _str = fd.readline()
    new_str = ""
    i = int(0)
    while i < len(_str):
        if _str[i].isalpha():
            liter = _str[i]
            nb = ""
            i+=1
            while i < len(_str) and _str[i].isdigit():
                nb+=_str[i]
                i += 1
            nb = int(nb)
            k = 0
            while k <  nb:
                new_str+=liter
                k+=1
        else:
            i +=1
    with open("result.txt", 'w') as fd:
        fd.write(new_str+"\n")
    print(new_str)
              
if __name__ == "__main__":
    rd()
    pass





