#coding=utf-8
# 通过Python编程完成一个银行ATM机模拟系统，具备如下功能:
# (1)登陆验证：用户输入用户名密码登陆，检测用户名是否存在以及用户名密码是否匹配；用户名密码各有三次输入机会，超过三次系统退出。
# (2)菜单界面：登陆成功后显示功能操作界面，输入序号选择对应功能。
# (3)用户注册：用户可以输入用户名和密码创建自己的账号，并输入电话号码等信息，如果用户名存在则让用户重新输入用户名。注册后免费赠送5000元余额。
# (4)账户管理：用户可以随时查看自己的账户余额。用户可以输入其他账户用户名，实现转账功能；用户名必须存在。用户也可以模拟实现存取款功能。
# (5)用户名和密码以及账户信息等必须永久保存。且基于命令行完成，不需要开发GUI界面。
import os
# print('欢迎进入Rachel的银行系统')
# print('请输入你要进行的')
# name=[]
#


def login():
    global chance
    user_name = input('请输入你的用户名：')
    while True:
        with open("user1.txt", "r") as g:
            name = eval(g.readline())
        if user_name=='' and  user_name.isspace():
            print('用户名不能为空')
            if user_name not in name.keys():
                print('用户名输入错误，请重新输入！')
                chance+=1
                if chance==3:
                    print('您已输入错误三次，请重新输入！')
        else:
            print('end')
            break

    #
    # chance=3
    # password = input('请输入你的密码：')
    # while True:
    #     if user_name == ' ':
    #         print('密码不能为空')
    #         if user_name in name:
    #             chance -= 1
    #             if chance != 0:
    #                 print('密码输入错误，请重新输入！')
    #             else:
    #                 print('您已输入错误三次，请重新输入！')
    #         else:
    #             print('登录成功！')
    #             print('请选择你要进行的操作！')
    #             print('1转载')

login()


