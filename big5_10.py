import pandas as pd
import requests
big5_url = 'https://www.taifex.com.tw/cht/3/largeTraderFutQry'
big5_table = pd.read_html(requests.get(big5_url, headers={'User-agent': 'Mozilla/5.0(Windows NT 6.1; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/63.0.3239.132 Safari/537.36'}).text)
big5_table[3]
big10_call = big5_table[3].iloc[2][5].split('%', 1)[0] #以%分割字串，分割1次,取出第一項
print(big10_call)
big10_put = big5_table[3].iloc[2][9].split('%', 1)[0]
print(big10_put)
dif_big10 = float(big10_call) - float(big10_put)
print('前十大差額{:.2f}%'.format(dif_big10) ) #浮點數取到小數後一位
big5_call = big5_table[3].iloc[2][3].split('%', 1)[0]
print(big5_call)
big5_put = big5_table[3].iloc[2][7].split('%', 1)[0]
print(big5_put)
dif_big5 = float(big5_call) - float(big5_put)
print('前五大差額{:.2f}%'.format(dif_big5))