# User will provide 2 numbers you have to find the HCF of those 2 numbers
a=int(input("Enter first number"))
b=int(input("Enter Second number"))
x_div=[]
y_div=[]
for i in range(1,a+1):
    if a%i==0:
        x_div.append(i)
for i in range(1,b+1):
    if b%i==0:
        y_div.append(i)
common_list=[]
for i in x_div:
    if i in y_div:
        common_list.append(i)
print(f"HCF of {a},{b} are",common_list)
        