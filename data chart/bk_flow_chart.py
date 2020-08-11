import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

pd.set_option('display.max_rows',100)
pd.set_option('display.max_columns',50)
pd.set_option('display.width',1000)

BK_Code='480'







"""
---------------设定图片布局和子图-----------------------------
"""
fig, (ax1, ax2 , ax3) = plt.subplots(3, 1, figsize=(10,3),sharex=True)
#fig, (ax1) = plt.subplots(3, 1, figsize=(5,3),sharex=True)   # ax1 爲子圖1




"""
-----     AX1         ---------------------------------
"""

#---设定AX1数据
df_bk_hist_flow=ts.get_bk_hist_capital_flow(BK_Code)
print(df_bk_hist_flow)


     #   設置 X,Y 的 值
X_Date_value=df_bk_hist_flow['date']

Y_Close_value=df_bk_hist_flow['main_buy'].astype(float)

    #    設置子圖樣式
ax1.plot(X_Date_value,Y_Close_value)

ax1.grid()

ax1.title.set_text(BK_Code + ' ' +'main_buy')




"""
-----     AX2         ---------------------------------
"""





#-----          其它设定         ---------------------------------
plt.xticks(rotation=45)
plt.xticks(horizontalalignment='right')    # 將 xlabel 靠右顯示

plt.show()
