st = input("Введите строку")
up=0
low=0
for i in range(0, len(st)-1, 1):
    if(st[i].isupper()==True and st[i+1].isupper()==True):
        up+=1
    if(st[i].islower()==True and st[i+1].islower()==True):
        low+=1
print(up)
print(low)