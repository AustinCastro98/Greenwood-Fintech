import numpy as pd 
import pandas as pd
import matplotlib.pyplot as plt
from docutils.utils.math.tex2unichar import space
from matplotlib import style 
 

#Cleaning the Data 
df = pd.read_csv('Chase.CSV')
df.set_index('Posting Date', inplace = True) 
df = df[['Details','Amount','Balance','Description']] 
df = df.tail(100) 
#print(df)
total_deposits = 0
total_withdrawal = 0

#Spacer Object
class Spacer:
    def __init__ (self,space,num_of_spaces):
        self.space = space
        self.num_of_spaces = num_of_spaces
    def __str__(self):
        return self.space * self.num_of_spaces

spacer = Spacer('\n',4)

#Printing information about Deposits.
for i in range(len(df['Details'])):
        if df.iloc[i,0] == 'CREDIT': 
            #print("Credit")
            #print(df.iloc[i,1], df.index[i], df.iloc[i,3])
            total_deposits += df.iloc[i,1] 
        elif df.iloc[i,0] == 'DSLIP': 
            #print("Credit") 
            #print(df.iloc[i,1], df.index[i], df.iloc[i,3])
            total_deposits += df.iloc[i,1]


#Printing Information about Withdraws.
for i in range(len(df['Details'])):
        if df.iloc[i,0] == 'DEBIT':
            #print('Debit')
            #print(df.iloc[i,1], df.index[i], df.iloc[i,3])
            total_withdrawal += df.iloc[i,1]

#print(spacer)

#Amount Totals
print('Total Amount of Deposits:', total_deposits) 
print("Total Amount of Withdrawals:",total_withdrawal)

#Creating list for ploting

Food = ['SHARK FISH AND CHI','WALGREENS','DOLLARTREE','REFRESHMENT SERVICES','CHICK-FIL-A','LITTLE CAESARS','TACO BELL','POPS ITALIAN BEEF SA','PORTILLOS','NEERU CITGO','SCOTTYS LINCOLN CARRYO','DAIRY QUEEN','MILLENNIUM NEWS & VIEWS CHICAGO IL','WALMART','JEWEL'] 
Shopping = ['GARY CAMERA & VIDEO','ZAO ISLAND','LORD & TAYLOR FREEHOLD', 'LORDANDTAYLOR.COM','Amazon','Isu Cupboard','FINISH-LINE','LUKE','PORTILLOS','BEST BUY','TJMAXX','LOWE','ADOBE'] 
Investments = ['Shopify','MONTHLY SERVICE FEE','USPS PO','FACEBK','BIG PICTURE',"LOW'S"] 
miscellaneous = ['Haircut','ATM FEE']
school = ['BIG PICTURE ','VITALSOURCE','ISU Barns'] 


catagory_list = [] 
#Creating a third column
df['Catagory'] = ""

for i in range(len(df['Description'])): 
    if df.iloc[i,3] in Food:
        df.iloc[i,4] ='Food' 
    elif df.iloc[i,3] in Shopping:
        df.iloc[i,4] = 'Shopping' 
    elif df.iloc[i,3] in Investments: 
        df.iloc[i,4] = 'Investment' 
    elif df.iloc[i,3] in miscellaneous: 
        df.iloc[i,4] = 'Miscellaneous'
    elif df.iloc[i,3] in school:
        df.iloc[i,4] = 'School'
    elif df.iloc[i,0] == 'DEBIT': 
        df.iloc[i,4] = 'Withdrawal' 
    elif df.iloc[i,0] == 'CREDIT': 
        df.iloc[i,4] = 'Deposit' 
    elif df.iloc[i,0] == 'DSLIP':
        df.iloc[i,4] = 'Credit' 
 


#obtaining indexes from Description list.
 
print(df) 

#Pie chart for 20/30/50 rule
percentages = [20,30,50]
catagories = ['Savings','Wants','Needs']
plt.figure(0)
plt.pie(percentages, labels=catagories, shadow = True, autopct = '%1.1f%%')



