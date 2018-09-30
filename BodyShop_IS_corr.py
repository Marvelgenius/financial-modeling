# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd

filepath=r'C:\Users\fanyu\Desktop\Test\Body Shop Analysis.xlsx'
IS = pd.read_excel(filepath,index_col='items')
temptput=r'C:\Users\fanyu\Desktop\Test\Body Shop Analysis_clean table.xls'
output=r'C:\Users\fanyu\Desktop\Test\Body Shop Analysis_corr.xls'

clean_table=pd.DataFrame([IS.iloc[:7,0],IS.iloc[:7,2],IS.iloc[:7,4]]).T
print(clean_table)
clean_table.to_excel(temptput)
corr_list=clean_table.T.corr()
corr_list.to_excel(output)
