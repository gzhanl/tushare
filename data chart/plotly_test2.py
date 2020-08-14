# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 12:33:44 2020

@author: DELL
"""
import plotly.plotly as py
import py.express as px

gapminder = px.data.gapminder()
gapminder2007 = gapminder.query('year == 2007')
px.scatter(gapminder2007, x='gdpPercap', y='lifeExp')