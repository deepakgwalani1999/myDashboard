# -*- coding: utf-8 -*-
import pandas as pd
data=pd.read_excel("articles.xlsx")
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

data.describe()
data.info()
no_of_article=data.groupby(["source_id"])["article_id"].count()
no_of_article
data.groupby(["source_id"])["engagement_reaction_count"].sum()
data.drop("engagement_comment_plugin_count",axis=1,inplace=True)



 
    
def keywordflag(k):
    keyword_flag=[]
    for i in data["title"]:
        try:
            if k in str(i):
                flag=1
            else:
                flag=0
        except:
            flag=0
        keyword_flag.append(flag) 
    return keyword_flag

k1=keywordflag("murder")

data["KeywordFlag"]=pd.Series(k1)

#sent_int=SentimentIntensityAnalyzer()
#text=data["title"][3]
#sent=sent_int.polarity_scores(text)

title_neg_sentiment=[]
title_pos_sentiment=[]
title_neu_sentiment=[]


for x in data["title"]:
    try:
        sent_int=SentimentIntensityAnalyzer()
        sent=sent_int.polarity_scores(x)
        neg=sent["neg"]
        pos=sent["pos"]
        neu=sent["neu"]
    except:
        neg=0
        pos=0
        neu=0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment=pd.Series(title_neg_sentiment)
title_pos_sentiment=pd.Series(title_pos_sentiment)
title_neu_sentiment=pd.Series(title_neu_sentiment)

data["title_neg_sentiment"]=title_neg_sentiment
data["title_pos_sentiment"]=title_pos_sentiment
data["title_neu_sentiment"]=title_neu_sentiment

data.to_excel("blog_me_cleaned.xlsx",sheet_name="blog_me",index=False)
