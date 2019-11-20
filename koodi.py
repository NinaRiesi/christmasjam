from pytrends.request import TrendReq
import csv
import pandas as pd
import numpy
import time
pytrend = TrendReq(hl='en-UK' , tz=0)
kw_list=['Last Cristmas']

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
#pytrend.build_payload(kw_list=['Last Cristmas'],geo='GB-SCT',gprop='youtube',timeframe='today 1-d')
pytrend.build_payload(kw_list=['Last Christmas','Jingle Bells'],geo='GB',gprop='youtube',timeframe='now 1-H')
interest_over_time_df = pytrend.interest_over_time()
print(interest_over_time_df.head())

names = ['x','y','z']
interest_over_time_df.columns = names
print(interest_over_time_df.head())

nLC=interest_over_time_df[['x','y']].sum()[0]
nJB=interest_over_time_df[['x','y']].sum()[1]


print(nLC)
print(nJB)

#x='Last Christmas'
#interest_over_time_df.loc['Total'] = pd.Series(interest_over_time_df['Last Christmas','Jingle Bells'].sum(), index = ['Last Christmas','Jingle Bells'])
#df.loc["Total", x] = df.x.sum()
#print (df)