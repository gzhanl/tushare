import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

pd.set_option('max_columns',50)


"""

------------在這裡輸入股票號碼--------------------------------

"""



Stock_NO='000858'

# df_hist_data=ts.get_hist_data(Stock_NO)
# df_hist_data=df_hist_data[0:100]
# print(df_hist_data)
#df_hist_date_high_low=df_hist_data.drop(columns=['B', 'C'])
#print(df_hist_date_high_low)

df_hist_capital_flow=ts.get_hist_capital_flow(Stock_NO)
print(df_hist_capital_flow.head(10))
print(df_hist_capital_flow.tail())


Buy_value=df_hist_capital_flow['superlarge_buy'].astype(float)*10000+df_hist_capital_flow['large_buy'].astype(float)*10000

Buy_value=Buy_value* 0.00000001

print('%s 主力淨買入=超大單淨買入,大單淨買入總額 : %f億'%(df_hist_capital_flow['date'][99],Buy_value[99]))


"""

---------------開始畫圖-----------------------------

"""

fig, (ax1, ax2 , ax3) = plt.subplots(3, 1, figsize=(5,3),sharex=True)

#-----          AX1         ---------------------------------

     #   設置 X,Y 的 值
X_Date_value=df_hist_capital_flow['date']

Y_Close_value=df_hist_capital_flow['close'].astype(float)

    #    設置子圖樣式
ax1.plot(X_Date_value,Y_Close_value)

ax1.grid()

ax1.title.set_text(Stock_NO + ' ' +'Close')



#-----          AX2         ---------------------------------

    #   設置 X,Y 的 值
X_Date_value=df_hist_capital_flow['date']

Y_Buy_value =df_hist_capital_flow['superlarge_buy'].astype(float)*10000+df_hist_capital_flow['large_buy'].astype(float)*10000

Y_Buy_value=Y_Buy_value* 0.00000001

Y_Buy_value[0]=Y_Buy_value[0]

   #   計算 累積淨買入
for i in range(1,100):
    Y_Buy_value[i]=Y_Buy_value[i-1]+Y_Buy_value[i]

    #    設置子圖樣式
ax2.plot(X_Date_value,Y_Buy_value,'orange')

ax2.grid()

ax2.title.set_text(Stock_NO + ' ' + 'Capital_Flow')




#-----          AX3         ---------------------------------

    #   設置 X,Y 的 值
X_Date_value=df_hist_capital_flow['date']

#Y_Buy_value =df_hist_capital_flow['superlarge_buy'].astype(float)*10000+df_hist_capital_flow['large_buy'].astype(float)*10000

Y_Buy_value=Y_Buy_value* 0.00000001

Y_Buy_value[0]=Y_Buy_value[0]

   #   計算 累積淨買入
for i in range(1,100):
    Y_Buy_value[i]=Y_Buy_value[i-1]+Y_Buy_value[i]

    #    設置子圖樣式
ax3.plot(X_Date_value,Y_Buy_value,'orange')

ax3.grid()

ax3.title.set_text(Stock_NO + ' ' + 'Flow')



# ------旋转45度显示
plt.xticks(rotation=45)
plt.xticks(horizontalalignment='right')    # 將 xlabel 靠右顯示








plt.show()

