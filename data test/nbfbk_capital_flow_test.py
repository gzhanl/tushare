# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:33:36 2020

@author: DELL
"""

"""
获取北向资金板块历史资金流
"""

import tushare as ts
import pandas as pd

pd.set_option('display.max_rows',100)
pd.set_option('display.max_columns',50)
pd.set_option('display.width',1000)



res=ts.get_nbfbk_hist_capital_flow('465')
print(res)
