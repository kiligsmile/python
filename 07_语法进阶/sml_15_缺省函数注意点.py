# 必须保证带有默认值的缺省参数在参数列表末尾
def print_info(name,title=" ",gender=True):
    """
    :param title:职位
    :param name: 班上同学的姓名
    :param gender: True男生 False女生
    """
    gender_text ="男生"
    if not gender:
        gender_text = "女生"
    print("[%s]%s是%s"%(title,name,gender_text))
# 假设班上的同学，男生居多！
# 提示：在指定参数的默认值时，应该使用最常见的值作为默认值！
print_info("小明")
# 在调用函数时，如果有多个缺省参数，需要指定参数名，这样解释器才能够知道参数的对应关系
print_info("拉拉",gender=False)