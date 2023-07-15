# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 18:18:21 2023

@author: welcome
"""
import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd
json_file=open("loan_data_json.json")
loan_df=json.load(json_file)
type(loan_df)

loandata=pd.DataFrame(loan_df)
loandata.info()
loandata["purpose"].unique()
loandata.describe()
loandata["int.rate"].describe()
loandata["fico"].describe()
loandata["dti"].describe()
income=np.exp(loandata["log.annual.inc"]) 
loandata["annual_income"]=income


# fico scores
fico_cat=[]
#fico=700
# testing error 
for  i in range(len(loandata["fico"])):
    category=loandata["fico"][i]
    
    try:
        if  category>=300 and  category<400:
                cat="Very poor"
        elif  category>=400 and  category<600:
            cat="Poor"
        elif  category>=601 and  category<660:
            cat="Fair"
        elif  category>=660 and  category<700:
            cat="Good"
        elif  category>=700:
            cat="Excellent"
        else:
            cat="Unknown"
    except:
        cat="Unknown"
    fico_cat.append(cat)  
fico_cat=pd.Series(fico_cat)
loandata["fico_cat"]=fico_cat    
   
loandata.loc[loandata["int.rate"]>0.12,"Int.rate.type"]="High"  
loandata.loc[loandata["int.rate"]<0.12,"Int.rate.type"]="Low"   

catplot=loandata.groupby(["fico_cat"]).size()
catplot.plot.bar(color="red" , width=0.1)
plt.show()
purposecountplot=loandata.groupby(["purpose"]).size()
purposecountplot.plot.bar(color="green",width=0.3)
plt.show()


#scatter plot

plt.scatter(x=loandata["dti"],y=loandata["annual_income"],color="black")
plt.show()

#writing in csv

loandata.to_csv("loan_cleaned.csv",index=True)
