# import pandas as pd
# paragraph , n=2
sentence = "a,b,c,d are going to school"
result = "a,b c,d are going to school"
n = 2


def remove_comma(n, sentence):
    count = 0
    temp_list = []
    for i in sentence:
        if i == "," and count != n:
            count = count + 1
            print(count)
        else:
            temp_list.append(i)
        if count == n:
            temp_list.append("")
    print(sentence)

    temp_list = "".join(temp_list)
    print(temp_list)


remove_comma(n, sentence)

# >>> s="a,b,c,d are going to school"
# >>> s1=s.split(',')
# >>> s1
# ['a', 'b', 'c', 'd are going to school']
# >>> sl=s1[0:2]
# >>> sl
# ['a', 'b']
# >>> sr=s1[2:]
# >>> sr
# ['c', 'd are going to school']
# >>> rs=','.join(sl)+' '+','.join(sr)
# >>> rs
# 'a,b c,d are going to school'
# >>> sr=s1[3:]
# >>> sl=s1[0:3]
# >>> rs=','.join(sl)+' '+','.join(sr)
# >>> rs
# 'a,b,c d are going to school'
