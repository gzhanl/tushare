import tushare as ts
import pandas as pd

from bokeh.plotting import figure, output_file, show

pd.set_option('display.max_rows',100)
pd.set_option('display.max_columns',50)
pd.set_option('display.width',1000)



# 獲取data
BK_Code='465'

df_nbfbk_hist_flow=ts.get_nbfbk_hist_capital_flow(BK_Code)
print(df_nbfbk_hist_flow)


     #   設置 X,Y 的 值
X_Date_value=df_nbfbk_hist_flow['date']
X_Date_value=pd.to_datetime(X_Date_value)

Y_mainbuy_value=df_nbfbk_hist_flow['znzjb'].astype(float)
Y_mainbuy_value=Y_mainbuy_value

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(tools="hover,pan,box_zoom,reset,save",title="simple line example", x_axis_label='date', y_axis_label='main_buy',plot_width=1500, plot_height=800, x_axis_type="datetime")

# add a line renderer with legend and line thickness
p.line(X_Date_value, Y_mainbuy_value, legend_label="今日持股占北向资金比.", line_width=2)

# show the results
show(p)