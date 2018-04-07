# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 09:27:53 2018

@author: 某树
"""

name=input("请输入您的姓名:")
if name in ("褚晓雪"):
    print("您好，{}小姐，主人给您留了一封信，请确定是否要开启？".format(name[0]))
    y=input()
    if y in ("快，好，打开，，好的，嗯"):
        print("丑晓雪，我喜欢你。")
if name in("抱木"):
    print("My master,can I help you?")
    x=input()
    if x in("嗯，好，email"):
        print("Whether to make changes to your mail?")
        x=input()
        if x in("不，不用了，没事"):
            print("好的，主人。")
    