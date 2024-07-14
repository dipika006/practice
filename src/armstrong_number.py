armstrong_list = []
for i in range(100, 1000):
    a = i % 10
    b = i // 10
    c = b % 10
    d = b // 10
    if (a**3 + c**3 + d**3) == i:
        armstrong_list.append(i)
    else:
        pass
print("Armstrong numbers are", armstrong_list)
