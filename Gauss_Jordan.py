n = int(input("Matritsa o'lchamini kiriting: "))
m = n
ls = []
while m != 0:
    l = input('qatorni kiriting: ')
    ls.append(list(int(i) for i in l.split()))
    m -= 1


for i in range(len(ls)):
    s = ""
    for j in range(len(ls[i])):
        s += ("+" * (ls[i][j] > 0 and j != 0) + '-' * (ls[i][j] == -1) + str(ls[i][j]) * (ls[i][j] != 1 and ls[i][j] != -1) + 'X' + str(j + 1)) * (ls[i][j] != 0)
    ls[i].append(int(input(s + " = ")))

for i in range(n):
    num = ls[i][i]
    for t in range(n + 1):
            ls[i][t] /= num
    
    for j in range(n):
       if j != i:
        number = ls[j][i]
        for k in range(n + 1):
                ls[j][k] += -number *  ls[i][k]

for p in ls:
    print(p)

for q in range(n):
    print(f"X{q + 1} = {ls[q][-1]}")