# Write a program to print whether a given number is prime number or not
def prime_check(n):
    # n=int(input("Enter a number to check prime or not"))
    new=[]
    if (n==1):
        print("1 is not a prime number")
        return 0
    for i in range(1,n+1):
        if(n%i)==0:
            new.append(i)
    if(len(new)>2):
        # print("it is not a prime number")
        return n
    else :
        # print("It is a prime number")
        return 0
prime_list=[]
for i in range (100,200):
    temp=prime_check(i)
    if temp==0:
        prime_list.append(i)
print("Prime numbers in between the range is",prime_list)