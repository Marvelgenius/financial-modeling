# -*- coding: utf-8 -*-

import pandas as pd
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt

filepath=r'C:\Users\fanyu\Desktop\Test\Body Shop Analysis_clean table.xls'
IS = pd.read_excel(filepath,index_col='items')

# to predict sales in the next 3yrs

sales_trained_y=IS.iloc[0,:]
sales_trained_x=pd.DataFrame([1999,2000,2001])
reg = linear_model.LinearRegression()
reg.fit(sales_trained_x,sales_trained_y)
print("Scores: \n",reg.score(sales_trained_x,sales_trained_y))
sales_predict_x=pd.DataFrame([2002,2003,2004])
sales_predict_y=reg.predict(sales_predict_x)
print("Coefficients: \n",reg.coef_)
print("The exp sales of the next 3 yrs: \n",sales_predict_y)

plt.scatter(sales_trained_x,sales_trained_y,color='black')
plt.plot(sales_predict_x,pd.DataFrame(sales_predict_y),color='blue',linewidth=3)
plt.ylabel('Sales in Million')
plt.xlabel('Years')
plt.title('Sales Prediction')
plt.grid()

plt.show()

# to predict the cost of sales of the next 3 yrs
def CsA(cost_g,sales_g):
    cost_std=cost_g.std()
    sales_std=sales_g.std()
    SalesCost_cov = pd.DataFrame([cost_g,sales_g]).T.cov().iloc[1,0]
    SalesCost_amp = SalesCost_cov / (sales_std ** 2)
    print("S&C amplifier is: ", SalesCost_amp)
    return SalesCost_amp
#function to calculate the cost growth rate and sales growth rate amplifier

cost_y=IS.iloc[1,:].values.tolist()
cost_g=[]
for i in range(0,len(cost_y)-1):
    Grate=cost_y[i+1]/cost_y[i]-1
    cost_g.append(Grate)
print("Cost growth: ",cost_g)
# Calculate the growth rate of cost
sales_g = []
for i in range(0,len(sales_predict_y)-1):
    Grate=sales_predict_y[i+1]/sales_predict_y[i]-1
    sales_g.append(Grate)
print("Sales growth: ",sales_g)
# Calculate the growth rate of sales
try:
    sales_g = pd.DataFrame(sales_g)
    cost_g = pd.DataFrame(cost_g)
    cost_Grate=pd.DataFrame(sales_g) * CsA(cost_g,sales_g)
    print(cost_Grate)
except KeyError as e:
    print(e)

# another way to predict
