user_input=input("Enter the full sentence")
a_list=user_input.split(' ')
a=[]
for i in a_list:
    a.append(len(i))
print(a_list[a.index(max(a))])