# put your python code here
nb = int(input())
nb_=nb
matrix = []
el = []
i = 0
j = 0
while j < nb:
    i = 0
    el = []
    while i < nb:
        el.append(int(0))
        i+=1
    matrix.append(el)
    j += 1
j = 0
i = 0
l = 1
break_flag = False
k = -1

while True:
    while i < nb:
        matrix[j][i] = l
        l+=1
        i+=1
    i-= 1
    j+=1
    #print(matrix)

    while j < nb:
        matrix[j][i] = l
        l+=1
        j+=1
    j-=1
    nb-=1
    i-=1
    #print(matrix)

    while i > k:
        matrix[j][i] = l
        l+=1
        i-=1
    i+=1
    k+=1
    #print(matrix)
    j-=1
    while j > k:
        matrix[j][i] = l
        l+=1
        j-=1
    j+=1
    i+=1
    #print(matrix)

    if l > nb_**2:
        break

#print(break_flag)
#print(i,j)
str_matrix = ""
i = 0
j = 0

while i < nb_:
    j = 0
    raw = ""
    while j  < nb_:
        raw+=str(matrix[i][j]) + " "
        j+=1
    i += 1
    print(raw)
    