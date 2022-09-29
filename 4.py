dict1 = {1: 1, 2: 9, 3: 4,4:99,5:7}
dict2 = {}
sortedk = sorted(dict1, key=dict1.get, reverse=True)
for i in sortedk:
    dict2[i]=dict1[i]
print (dict2)