#Art Tenorio
#CISC483

import csv
import numpy as np
import pandas as pd

df = pd.read_csv("/home/art/Downloads/data.csv",
skiprows=0)
#dataset attr names would mess up without this
df.columns=df.columns.str.strip()
#had to rename the class attribute, since class is a keyword somewhere in python
df.rename(columns={'class' : 'classmoney'}, inplace=True)
df.columns=df.columns.str.strip()
#print(df.columns)
#print(df.head(10))
print(df.dtypes)  
print("Not all columns are numerical, so they must be converted.\n") 
#convert sex to binary values. Makes sex to int64 type
sex = {'Male' : 0, 'Female': 1}
df.sex = [sex[item] for item in df.sex]
#convert classmoney object to int64 in binary 
money = {'<=50K' : 0, '>50K' : 1}
df.classmoney = [money[item] for item in df.classmoney]
print(df.head(8))
#next, convert race to integer, based on classmoney attr value
df.loc[df.classmoney == 0, ['race']] = 0
df.loc[df.classmoney == 1, ['race']] = 1
print(df.dtypes)   
print("finally all the columns for the matrices are numerical.\n")
#finally, we want the covariance and correlation matrices
#using: age, education-num,race,sex,capital-gain,capital-loss,
#hours-per-week, class

newdf = df[['age','education-num','race','sex','capital-gain',
'capital-loss','hours-per-week','classmoney']].copy()



print('COVARIANCE MATRIX:')
cov = newdf.cov()
print(cov)
print('\n')
print('CORRELATION MATRIX:')
corr = newdf.corr()
print(corr)
print('\n')
