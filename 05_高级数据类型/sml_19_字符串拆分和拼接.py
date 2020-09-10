# 假设：一些内容是从网络上抓取的
# 要求：
# 1.将字符串中的空白字符全部去掉
# 2.再使用" "作为分隔符，拼接成一个整齐的字符串
poem_str="登鹳雀楼\t王之涣\t白日依山尽\t\n黄河入海流\n欲穷千里目\n\t更上一层楼"
print(poem_str)

# 1.拆分字符串
poem_list=poem_str.split()
print(poem_list)

# 2.合并字符串
result=" ".join(poem_list)
print(result)
# 注意：使用" "、\n、\t 等均可作为字符串