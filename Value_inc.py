# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 17:50:15 2023

@author: welcome
"""

import pandas as pd
trs_df=pd.read_csv("transaction2.csv",sep=";")
#trs_df.info()
#CostPerItem=11.73
#SellingPricePerItem=21.1
#NumberOfItemsPurchased=6
#ProfitPerItem=21.1-11.73
#print(ProfitPerItem)


#OR

#ProfitPerItem=SellingPricePerItem-CostPerItem
#ProfitPerTransaction=NumberOfItemsPurchased*ProfitPerItem
#SelllingPerTransaction=NumberOfItemsPurchased*SellingPricePerItem
#CostPerTransaction=NumberOfItemsPurchased*CostPerItem


#CostPerItem
CostPerItem=trs_df["CostPerItem"]

# Number Of Item Purchased
NumberOfItemsPurchased=trs_df["NumberOfItemsPurchased"]

#SeelinPricePerItem
SellingPricePerItem=trs_df["SellingPricePerItem"]
# CostPerTransaction=cost*Items
CostPerTransaction=CostPerItem*NumberOfItemsPurchased
trs_df["CostPerTransaction"]=CostPerTransaction
#Selling Per Transaction=selling*items
trs_df["SelllingPerTransaction"]=trs_df["SellingPricePerItem"]*trs_df["NumberOfItemsPurchased"]
#ProfitPerTransaction=SellingPerTransaction-CostPerTransaction
trs_df["ProfitPerTransaction"]=trs_df["SelllingPerTransaction"]-trs_df["CostPerTransaction"]
#MarKup=(SPT-CPT)/CPT
trs_df["Markup"]=(trs_df["SelllingPerTransaction"]-trs_df["CostPerTransaction"])/trs_df["CostPerTransaction"]
# Roundingvalues of markup upto 2 decimal places
roundMarkup=round(trs_df["Markup"],2)
trs_df["Markup"]=roundMarkup

#Converting Year To string
year=trs_df["Year"].astype(str)
print(year.dtype)

#Converting Day To string
day=trs_df["Day"].astype(str)
print(day.dtype)
date=day+"-"+trs_df["Month"]+"-"+year
trs_df["date"]=date
#trs_df.iloc[0]
#trs_df.iloc[0:4]
#trs_df.iloc[-5:-1]
#trs_df.iloc[0:4,2]

#Splitting Client Keywords
split_keywords=trs_df["ClientKeywords"].str.split(',' , expand=True)

#Assigning this to data of transaction
trs_df["Client_Age"]=split_keywords[0] 
trs_df["Client_type"]=split_keywords[1]
trs_df["Length_of_Contract"]=split_keywords[2]

#Removing Brackets from Clients age
trs_df["Client_Age"]=trs_df["Client_Age"].str.replace("[","")

#Removing Brackents from Length of Contact Column
trs_df["Length_of_Contract"]=trs_df["Length_of_Contract"].str.replace("]","")

# Making Item Description in Lower Keywords
trs_df["ItemDescription"]=trs_df["ItemDescription"].str.lower()

# Bringing new File to the data set i.e Season
season_df=pd.read_csv("value_inc_seasons.csv")

#Splitting season Data Month:Season
new_season=season_df["Month;Season"].str.split(';',expand=True)
#assigning to new Season dataframe
season_df["Month"]=new_season[0]
season_df["Season"]=new_season[1]

#drop Moth;Season Column
season_df.drop(["Month;Season"],axis=1,inplace=True)
#season_df.drop(["Status"],axis=1,inplace=True)

#Merging main dataframe and season DataFrame Mapping is dong inside of it only
trs_df=pd.merge(trs_df,season_df,on="Month")


#Dropping unecessary data from main dataframe
trs_df.drop(["ClientKeywords","Day","Year","Month"],axis=1,inplace=True)


#Export in csv
trs_df.to_csv("ValueInc_Cleaned.csv",index=False)