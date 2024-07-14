# import pandas as pd
# paragraph , n=2
sentence = "a , b , c , d are going to school"
result = "a,b c,d are going to school"
n = 2


def remove_comma(n, sentence):
    n = n
    count = 0
    temp_list = []
    for i in sentence:
        if i == ",":
            count = count + 1
            print(count, n)
        if count == n and i == ",":
            temp_list.append(" ")
        else:
            temp_list.append(i)
        # else:
        #     temp_list.append(i)
        # if(count==n):
        #    temp_list.append(',')
    print(sentence)
    temp_list = "".join(temp_list)
    print(temp_list)


remove_comma(n, sentence)
