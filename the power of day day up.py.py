a=eval(input())
b=(1+0.001*a)**365
c=(1-0.001*a)**365
print("你的输入为千分之{}。\n天天向上结果为：{:.2f}。\n天天放任结果为：{:.2f}。".format(a,b,c))

