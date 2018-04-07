TempConvert = input("请输入带有符号（C或F）的温度值，如99F：")
while TempConvert not in ("end,END，End"):
    if TempConvert[-1]in("F,f"):
        C = (eval(TempConvert[:-1])-32)/1.8                  #切片更加简洁
        print("转换后的温度是：摄氏{:.2f}度。".format(C))
    elif TempConvert[-1]in("C,c"):
        F = eval(TempConvert[:-1])*1.8+32
        print("转换后的温度是：华氏{:.2f}度。".format(F))
    else :
        print("输入格式错误，请重新输入！")
    TempConvert = input("请输入带有符号(C或F)的温度值，如99F：")   #增加条件循环可以持续运行，更加人性化。
                                                             #试试封装这个温度转换函数。
    
