import tushare as ts
import pandas as pd

pd_display_rows = 100
pd_display_cols = 100
pd_display_width = 1000
pd.set_option('display.max_rows', pd_display_rows)
#pd.set_option('display.min_rows', pd_display_rows)
pd.set_option('display.max_columns', pd_display_cols)
pd.set_option('display.width', pd_display_width)
pd.set_option('display.max_colwidth', pd_display_width)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('expand_frame_repr', False)


# res=ts.get_All_Stock_HK_Shareholding_Hist()
#
# res.to_csv('C:\\Users\\DELL\\Desktop\\Data_Web\\沪深股通持股记录多日.csv')


# token='67bcc08d60c4287441a1a80dd58701c5fd2d2c916bbf6758bb9cc05d'
# pro=ts.pro_api(token)
#
# res1=pro.hk_hold(trade_date='20210201',exchange='SH')
# res2=pro.hk_hold(trade_date='20210201',exchange='SZ')
#
# res=pd.concat([res1,res2])
# ts.Trans_HKCODE_to_ACODE('002025')

# res=ts.get_All_Stock_HK_Shareholding_Hist_CSV()
token = '67bcc08d60c4287441a1a80dd58701c5fd2d2c916bbf6758bb9cc05d'
pro = ts.pro_api(token)

res1 = pro.hk_hold(trade_date='20210201', exchange='SH')
res2 = pro.hk_hold(trade_date='20210201', exchange='SZ')

res = pd.concat([res1, res2])

res.to_csv('C:\\Users\\DELL\\Desktop\\Data_Web\\沪深股通代码.csv')
print(res)