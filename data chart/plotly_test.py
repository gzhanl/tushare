# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:56:01 2020

@author: DELL
"""

import plotly.express as px

df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
fig.show()