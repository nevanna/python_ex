def update_dictionary(d, key, value):
    if d.get(key) != None:
        d[key].append(value)
    elif d.get(key) == None:
        if d.get(2*key) != None:
            d[2*key].append(value)
        else:
            d[2*key]=[value]

def use():
    d = {}
    print(update_dictionary(d, 1, -1))  # None
    print(d)                            # {2: [-1]}
    update_dictionary(d, 2, -2)
    print(d)                            # {2: [-1, -2]}
    update_dictionary(d, 1, -3)
    print(d)                            # {2: [-1, -2, -3]}
    update_dictionary(d, 4, -3)
    print(d)         
if __name__ == "__main__":
    use()
    pass