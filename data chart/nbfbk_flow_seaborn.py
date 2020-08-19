import tushare as ts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows',100)
pd.set_option('display.max_columns',50)
pd.set_option('display.width',1000)


sns.set(style="darkgrid")


# 獲取data
BK_Code='480'

df_nbfbk=ts.get_nbfbk_hist_capital_flow(BK_Code)
print(df_nbfbk)

ax = sns.lineplot(x="date", y="szzf", data=df_nbfbk)