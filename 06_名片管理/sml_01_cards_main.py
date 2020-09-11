#! /usr/local/bin/python3
import sml_01_cards_tools
while True:
# 无限循环，由用户主动决定什么时候退出循环！
    # TODO 显示功能菜单
    sml_01_cards_tools.show_menu()
    action_str = input("请输入希望执行的操作: ")
    print("你选择的操作是【%s】"% action_str)
    # 1，2，3针对名片的操作
    if action_str in ["1","2","3"]:
        # 新增名片
        if action_str == "1":
            sml_01_cards_tools.new_card()
        elif action_str == "2":
            sml_01_cards_tools.show_all()
        elif action_str == "3":
            sml_01_cards_tools.search_card()
        # 如果在开发程序时，不希望立刻编写分支内部的代码
        # 可以使用pass关键字，表示一个占位符，能够保证程序的代码结构正确
        #程序运行时，pass关键字不会执行任何的操作！

    # 0退出系统
    elif action_str =="0":
        print("欢迎再次使用【名片管理系统】")
        # pass
        break

    # 其他内容输入错误，需要提示用户
    else:
        print("您输入的不正确，请重新选择")