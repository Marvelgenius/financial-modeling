import pandas as pd
import numpy as np

A=[]
B=[4,5,6]
for i in range(0,len(B)):
    A.append(B[i])
A=pd.DataFrame(A)
print(A*2)
