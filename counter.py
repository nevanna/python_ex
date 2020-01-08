st_ = str(input()).lower()
l = {}
st_ = st_.split(" ")
for word in st_:
    if word in l:
        l[word]+=1
    else:
        l[word] = 1
for k in l:
    print(k, l[k])

    