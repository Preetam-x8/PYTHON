import pandas as pd

#create series
s=pd.Series([10,20,30,40,50])

print("Series:")
print(s)

#Indexing
print("First Element :",s[0])

#Slicing
print("Slice:")
print(s[1:4])

#Query
print("Valuse Greater than 25:")
print(s[s>25])
