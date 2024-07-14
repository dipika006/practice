# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
n=int(input("Enter 4 digit number"))
a=n%10
b=n//10
c=b%10
d=b//10
e=d%10
f=d//10
reverse=1000*a+100*c+10*e+f
print(reverse)
