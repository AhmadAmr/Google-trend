from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US')

kw_list = ["spinner"]
data= pytrends.get_historical_interest(kw_list, 
                                        cat=0, geo='', gprop='', sleep=0)

data = data.drop(labels=['isPartial'],axis='columns')
data.to_csv('historical_interest.csv', encoding='utf_8_sig')