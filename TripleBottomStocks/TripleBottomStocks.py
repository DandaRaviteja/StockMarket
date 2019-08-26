import pandas as pd
from nsetools import Nse
nse = Nse()
selected_stocks=[]
link = 'https://chartink.com/eodscanner/Triple-Bottom.html'
dfs = pd.read_html(link)
df = pd.concat(dfs)
df = (df[1].iloc[3:]).tolist()
stocks = [x for x in df if x != 'nan']
all_stock_codes = nse.get_stock_codes()

selected_stocks=[]

for eachStock in stocks:
    for Key, Value in all_stock_codes.items():
            if str(eachStock) == Value:
                    selected_stocks.append(Key)
            else:
                if str(eachStock) not in all_stock_codes.values():
                    selected_stocks.append(str(eachStock))
                    break;
selected_stocks = [incom for incom in selected_stocks if str(incom) != 'nan']
print('TBL -->'+str(selected_stocks))
