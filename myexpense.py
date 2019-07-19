import numpy as pd 
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib import style 
 

#Cleaning the Data 
df = pd.read_csv('Chase.CSV')
df.set_index('Posting Date', inplace = True) 
df = df[['Details','Amount','Balance','Description']] 
df = df.tail(100) 
print(df)
total_deposits = 0
total_withdraw = 0 
for i in range(len(df['Details'])):
        if df.iloc[i,0] == 'CREDIT': 
            print("Credit")
            print(df.iloc[i,1])
            total_deposits += df.iloc[i,1] 
        elif df.iloc[i,0] == 'DSLIP': 
            print("Credit") 
            print(df.iloc[i,1]) 
            total_deposits += df.iloc[i,1]
        else:
            total_withdraw += df.iloc[i,1] 


print('Total Amount of Deposits:', total_deposits) 
print("Total Amount of Withdraws:",total_withdraw) 
'''
#calculating the total income 
#turing all the str values of the amount into floats
df['Amount'] = df.Amount.fillna(0).astype(float)
total_credit = 0 
for i in df['Amount']:
    total_credit += i
   # print(i) 
print(total_credit) 


#Filtering all credit transactions and listing amount of debit and credit transactions
debit = [] 
credit = []
num = 0
for i in df['Details']:
    if i == 'CREDIT':
       # print('Transaction info:',df.iloc[int(num),2],'Amount:\t', df.iloc[int(num),3])   
        credit.append(i) 
    else:
        debit.append(i)
    num+=1
print(len(debit)) 
print(len(credit))

print(df.columns)
'''
