def count_marks(l, subjects):
    new_l = l.split(';')
    len_ = len(new_l)
    new_str = []
    for t in new_l[1:]:
        new_str.append(int(t))
    sum_ = sum(new_str)
    mediana = round( (sum_ / (len_ - 1)), 9)
    for el in range(1,len_):
        if subjects.get(el) == None:
            subjects[el] = int(new_l[el])
        else:
            subjects[el] += int(new_l[el])

    return mediana


def start():
    file_name = input()
    subjects = {}
    fd_res = open("rez2.txt", 'a')
    i = 0
    with open(file_name, 'r') as fd:
        for l in fd:
            l = l.strip()
            i+=1
            print(str(count_marks(l, subjects)), file=fd_res)
    last_str = ""
    for k in range(1, len(subjects.keys()) + 1, 1):
        mark_ = round(subjects[k] / i, 9)
        last_str += str(mark_) + " "
    print(last_str, file=fd_res)
    fd_res.close()
        

if __name__ == "__main__":
    start()
    pass