import tushare as ts
import pandas as pd

pd.set_option('display.max_rows',100)
pd.set_option('display.max_columns',50)
pd.set_option('display.width',1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


res=ts.get_nf_realtime( )

# res=ts.get_nbfbk_hist_capital_flow('KB477')
print(res)

# print(res[0])
# print(res[1])
