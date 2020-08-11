import tushare as ts
import pandas as pd

pd.set_option('display.max_rows',100)
pd.set_option('display.max_columns',50)
pd.set_option('display.width',1000)



res=ts.get_bk_hist_capital_flow('433')
print(res)