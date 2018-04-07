tempconvert = input("请输入带有符号（C或F）的温度值，如99F：")
if tempconvert[-1]in("F,f"):
        C = (eval(tempconvert[0:-1])-32)/1.8
        print("转换后的温度是：{:.2f}C。".format(C))
elif tempconvert[-1]in("C,c"):
        F = eval(tempconvert[0:-1])*1.8+32
        print("转换后的温度是：{:.2f}F。".format(F))
else :
        print("输入格式错误，请重新输入！")#增加容错输入，以及易读的变量名称，但是，如果持续输入转化温度呢？
