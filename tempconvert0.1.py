x=input("请输入以符号C或F开头的温度值：")          #eval()无法转化字母或特殊符号混数字的字符串。
if x[0]=="C":                                      #此处布尔判断的是字符串，故需加引号表示str。
    F=eval(x[1:])*1.8+32                           #切片后才能计算。
    print("转换后的温度为：F{:.2f}。".format(F))   #不够人性化，变量名称缺少阅读意义，符号意义需要判断，没有考虑到用户的容错输入。
else:
    C=(eval(x[1:])-32)/1.8
    print("转换后的温度为：C{:.2f}。".format(C))