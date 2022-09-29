a = int(input("Введите число"))
a = str(a)
s = 0
for i in range(0, len(a), 1):
    if int(a[i]) % 2 != 0:
        s = s + int(a[i])
print(s)
