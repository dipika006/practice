#empty series
import pandas as pd
import numpy as np
# ser=pd.Series()
# print(ser)
# data=np.array(['D','I','P','I','K','A'])
# dict={'A':100,
#       'B':'Dipika',
#       'C':400}
# ser=pd.Series(data,index=[10,11,12,13,14,15])
# ser_dic=pd.Series(dict)
# print(ser_dic)
# print(type(ser_dic['A']),type(ser_dic['B']))
# print(ser)
# df=pd.DataFrame()
# data=[1,2,3,4,70,40]
# df=pd.DataFrame(data,columns=['amount'])
# print(df)

# program to depict shallow copy
# in pandas dataframe
 
# import module
# program to depict shallow copy
# in pandas dataframe
 
# import module
# import pandas as pd
 
# # assign dataframe
# df = pd.DataFrame({'index': [1, 2, 3, 4],
#                    'GFG': ['Mandy', 'Ron', 'Jacob', 'Bayek']})
 
 
# # shallow copy
# copydf = df.copy(deep=False)
 
# # comparing shallow copied dataframe
# # and original dataframe
# print('\nBefore Operation:\n', copydf == df)
 
# # assignment operation
# copydf['index'] = [0, 0, 0, 0]
 
 
# # comparing shallow copied dataframe
# # and original dataframe
# print('\nAfter Operation:\n', copydf == df)
 
# print('\nOriginal Dataframe after operation:\n', df)

# import pandas package as pd
import pandas as pd

# Define a dictionary containing students data
data = {'Name': ['Sneha', 'Shreya',
				'Sabhya', 'Riya'],
		'Age': [22, 18, 10, 19],
		'Stream': ['Computer', 'Commerce',
				'Arts', 'Mechanical'],
		'Percentage': [89, 93, 97, 73]}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age',
								'Stream', 'Percentage'])

# print("Given Dataframe :\n", df)

# print("\nIterating over rows using iterrows() method :\n")

# iterate through each row and select
# # 'Name' and 'Age' columns respectively.
# for index, row in df.iterrows():
# 	print(row["Name"], row["Age"])


# for index,row in df.iterrows():
#     print(row['Name'])
df=df.sort_values(by="Age", ascending=False)
print(df)