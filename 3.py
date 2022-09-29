list=[1612,49,'hello',6,19,'world']
sn=0
glas=0
soglas=0
for i in range(0, 5):
    if (type(list[i])==int):
        if(int(list[i]) % 2 == 0):
            for j in range(0, len(str(list[i])), 1):
                sn = sn + list[i]
        else:
            list[i]=1
    else:
        string=str(list[i])
        for k in range(0, len(string), 1):
            if (string[k] == "a" or string[k] == "e" or string[k] == "i" or string[k] == "o" or string[k] == "u" or string[k] == "y"):
                glas+=1
            else:
                soglas+=1
        print ("Элемент",i, glas,"Гласных и", soglas, "Согласных")
for a in range (0,6):
    print(list[a])