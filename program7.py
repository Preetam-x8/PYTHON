import numpy as np

#create array
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])

#Element-wise addition
print("Addition:",a+b)
print("Difference:",a-b)
print("Product:",a*b)

#Reshape array
c=a.reshape(2,2)
print("Reshaped Array:")
print(c)

print(np.zeros((2,3),dtype=int))
print(np.ones((3,2)))
print(np.arange(3,10))
print(np.linspace(0,1,5))
      

