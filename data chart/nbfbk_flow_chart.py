import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tushare as ts
import datetime as dt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from datetime import datetime


pd.set_option('display.max_rows',100)
pd.set_option('display.max_columns',50)
pd.set_option('display.width',1000)


sns.set(style="darkgrid")


# 獲取data
BK_Code='480'

df_nbfbk=ts.get_nbfbk_hist_capital_flow(BK_Code)
print(df_nbfbk)
"""
---------------開始畫圖-----------------------------

"""

fig, (ax1, ax2 , ax3) = plt.subplots(3, 1, figsize=(5,3),sharex=True)

#-----          AX1         ---------------------------------

     #   設置 X,Y 的 值
X_Date_value=df_nbfbk['date']
print(X_Date_value)
X_Date_value=pd.to_datetime(X_Date_value)
Y_cgbkb_value=df_nbfbk['cgbkb'].astype(float)

    #    設置子圖樣式
ax1.plot(X_Date_value,Y_cgbkb_value)

ax1.grid()

ax1.title.set_text(BK_Code + ' ' +'今日持股板块比')

#
# #-----          AX2         ---------------------------------
#
#     #   設置 X,Y 的 值
# X_Date_value=pd.to_datetime(df_nbfbk['date'])
#
# Y_Buy_value =df_nbfbk['znzjb'].astype(float)
#
# #Y_Buy_value=Y_Buy_value* 0.00000001
#
# #Y_Buy_value[0]=Y_Buy_value[0]
#
#
#
#     #    設置子圖樣式
# ax2.plot(X_Date_value,Y_Buy_value,'orange')
#
# ax2.grid()
#
# ax2.title.set_text(BK_Code + ' ' + '今日持股占北向资金比')
#
#
#
# """
# #-----          AX3         ---------------------------------
#
#     #   設置 X,Y 的 值
# X_Date_value=df_nbfbk['date']
#
# #Y_Buy_value =df_hist_capital_flow['superlarge_buy'].astype(float)*10000+df_hist_capital_flow['large_buy'].astype(float)*10000
#
# Y_Buy_value=Y_Buy_value* 0.00000001
#
# Y_Buy_value[0]=Y_Buy_value[0]
#
#    #   計算 累積淨買入
# for i in range(1,100):
#     Y_Buy_value[i]=Y_Buy_value[i-1]+Y_Buy_value[i]
#
#
#
#
#     #    設置子圖樣式
# ax3.plot(X_Date_value,Y_Buy_value,'orange')
#
# ax3.grid()
#
# ax3.title.set_text(Stock_NO + ' ' + 'Flow')
# """
#
#
# # ------旋转45度显示
# plt.xticks(rotation=45)
# plt.xticks(horizontalalignment='right')    # 將 xlabel 靠右顯示