import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import pandas as pd

Beiersdorf_years=pd.DataFrame([1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009])
Beiersdorf_sales= pd.DataFrame([1980,2242,2590,2955,3167,3136,3840,4041,4327,4661,5125,5011])
reg_Bei=linear_model.LinearRegression()
reg_Bei.fit(Beiersdorf_sales)
coef_Bei=reg_Bei.coef_
cov_Bei=Beiersdorf_sales.std()

Beiersdorf_sales=pd.DataFramed

PG_years=pd.DataFrame([1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009])
PG_sales= pd.DataFrame([37154,38125,39951,39244,])
reg_PG=linear_model.LinearRegression()
reg_PG.fit(PG_sales)
coef_PG=reg_PG.coef_
cov_PG=PG_sales.std()




plt.figure(1)
plt.plot(Beiersdorf_years,Beiersdorf_sales)
plt.xlabel('Yrs')
plt.ylabel('Sales')
plt.color('blue')
plt.grid()
plt.show()

plt.figure(2)
