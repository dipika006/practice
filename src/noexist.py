l1 = [4, 5, 6, 7, 8, 9, 20]
n = int(input("Enter the number"))
for i in l1:
    if i == n:
        print("number is present in the list")
        break
else:
    print("number is not present in the list")
