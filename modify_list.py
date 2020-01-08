


def modify_list(l):
    print(l)
    for i in range(len(l)-1, -1, -1):
        if l[i] % 2 == 0:
            l[i] = l[i] // 2
        else:
            l.pop(i)
        print(l)
def n():
    l_ = [1,2,3,4,5]
    print(l_)
    modify_list(l_)
    print(l_)

if __name__ == "__main__":
    n()
    pass