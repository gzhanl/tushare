# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 22:36:48 2020

@author: DELL
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 00:40:53 2020

@author: DELL
"""

import requests


'''               Sample code
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
'''


header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}  # my browser

#url='https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=阿里巴巴'
url="http://push2his.eastmoney.com/api/qt/stock/fflow/daykline/get?secid=90.BK0480&fields1=f1,f2,f3,f7&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65"
res=requests.get(url,headers=header).text

print(res)