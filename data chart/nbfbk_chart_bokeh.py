import tushare as ts
import pandas as pd

from bokeh.plotting import figure, output_file, show

pd.set_option('display.max_rows',100)
pd.set_option('display.max_columns',50)
pd.set_option('display.width',1000)


"""
酿酒行业:477   医药制造:465  家电行业:456   银行:475  电子元件:459  食品饮料:438  保险:474  机械行业:545  医疗行业: 727  
券商信托:473   软件服务:737  汽车行业:481   房地产:451  水泥建材:424 旅游酒店:485
"""
# 獲取data
BK_Code='545'

df_nbfbk_hist_flow=ts.get_nbfbk_hist_capital_flow(BK_Code)
print(df_nbfbk_hist_flow)


     #   設置 X,Y 的 值
X_Date_value=df_nbfbk_hist_flow['date']
X_Date_value=pd.to_datetime(X_Date_value)

Y_znzjb_value=df_nbfbk_hist_flow['znzjb'].astype(float)*10
Y_cgbkb_value=df_nbfbk_hist_flow['cgbkb'].astype(float)*100
Y_cgsz_value=df_nbfbk_hist_flow['cgsz'].astype(float)*10

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(tools="hover,pan,box_zoom,reset,save",title="simple line example", x_axis_label='date', y_axis_label='main_buy',plot_width=1500, plot_height=800, x_axis_type="datetime")

# add a line renderer with legend and line thickness
p.line(X_Date_value, Y_znzjb_value, legend_label="持股占北向资金比.", line_width=4,color='red')
p.line(X_Date_value, Y_cgbkb_value, legend_label="今日持股占板块比.", line_width=4,color='blue')
#p.line(X_Date_value, Y_cgsz_value, legend_label="今日持股市值.", line_width=4,color='green')
# show the results
show(p)