import pandas as pd
from nsetools import Nse
nse = Nse()
selected_stocks=[]

link = 'https://chartink.com/eodscanner/Triple-Bottom.html'
dfs = pd.read_html(link)
df = pd.concat(dfs)
df = (df[1].iloc[3:]).tolist()
stocks = [x for x in df if x != 'nan']

#get all stock codes
all_stock_codes = nse.get_stock_codes()
for eachStock in stocks:
        for Symbol, Name in all_stock_codes.items():
                if str(eachStock) == Name:
                    selected_stocks.append(Symbol)
print("tripleBottom --> "+str(selected_stocks))

