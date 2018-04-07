# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 09:58:04 2018

@author: 某树
"""

from datetime import datetime
now=datetime.now()
print(now)
day=now.strftime("%j")
print("当前为第{}天。".format(day))
