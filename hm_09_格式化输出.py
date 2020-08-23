# 定义字符串变量 name，输出 我的名字叫 小明，请多关照！
name = "拉拉"
print("我的名字叫%s，请多多关照！"%name)
# 定义整数变量 student_no,输出 我的学号是 000001
student_no = 1
print("我的学号是%06d"%student_no)
# 定义小数 price、weight、money。
# 输出 苹果单价9.00元/斤，购买了5.00斤，需要支付45.00元
price = 8.5
weight = 7.5
money = price*weight
print("苹果单价 %.2f元/斤，购买了%.2f，需要支付%.2f元"%(price,weight,money))
# 定义一个小数 scale，输出 数据比例是 10.00%
# 数据比例是10.00%
scale = 0.1
print("数据比例是%.2f%%"%(scale*100))
# 数据比例是10.000000%
scale = 0.1
print("数据比例是%f%%"%(scale*100))
# 数据比例是10.00%
scale = 0.1*100
print("数据比例是%.2f%%"%scale)
# 数据比例是0.10%×10
scale = 0.1
print("数据比例是%.2f%%"%scale*10)


