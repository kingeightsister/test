# coding=utf-8
# 通过Python编程完成一个银行ATM机模拟系统，具备如下功能:
# (1)登陆验证：用户输入用户名密码登陆，检测用户名是否存在以及用户名密码是否匹配；用户名密码各有三次输入机会，超过三次系统退出。
# (2)菜单界面：登陆成功后显示功能操作界面，输入序号选择对应功能。
# (3)用户注册：用户可以输入用户名和密码创建自己的账号，并输入电话号码等信息，如果用户名存在则让用户重新输入用户名。注册后免费赠送5000元余额。
# (4)账户管理：用户可以随时查看自己的账户余额。用户可以输入其他账户用户名，实现转账功能；用户名必须存在。用户也可以模拟实现存取款功能。
# (5)用户名和密码以及账户信息等必须永久保存。且基于命令行完成，不需要开发GUI界面。
import json

with open("custominfo.json") as f:
    r = json.load(f)
    print(r)


def main():
    while True:
        print('请输入序号选择你要进行的操作')
        print('1.登录\n', '2.注册\n', '3.退出\n')
        chioce = input('请输入序号：')
        if chioce == '1':
             login()
        if chioce == '2':
             register()
        if chioce == '3':
            return exit()


def register():
    username=input('请输入用户名')
    if username in r:
        print('用户名已存在！')
        # register()
        return
    password=input('请输入密码')
    r[username]=[password,5000]
    update()
    print('注册成功，免费赠送5000余额！')

def login():
    count = 3
    while True:
        username = str(input('请输入你的用户名：'))
        if username not in r:
            print('该用户名不存在，重新输入')
            count -= 1
            if count == 0:
                print('输入次数过多，请重新输入')
                return login()
        else:
            break
    count=3
    while True:
        password = str(input('请输入你的密码：'))
        if password == r[username][0]:
            print('登录成功')
            return show(username)
        else:
            if password not in r[username][0]:
                print('密码输入错误，请重新输入')
                count-=1
            if count == 0:
                print('输入次数过多，请重新输入')
                break

def show(username):
    while True:
        print('请输入您要选择的操作')
        print('0.回到首页\n1.查看当前余额\n2.转账\n3.存款\n4.取款\n5.退出\n')
        chance = input('请输入序号：')
        if chance=='0':
            main()
        if chance == '1':
            print(r[username][1])
        if chance == '2':
            uid = input('请输入其他用户的用户名：')
            if uid not in r:
                print('用户名不存在，请重新输入！')
                show(username)
            else:
                m = int(input('输入转账金额'))
                r[username][1] = r[username][1] - m
                r[uid][1] = r[uid][1] + m
                update()
                print('转账后余额为：', r[username][1])
        if chance=='3':
            m=int(input('请输入存款金额:'))
            r[username][1]=r[username][1]+m
            print('当前余额:',r[username][1])
            update()
        if chance=='4':
            m=int(input('请输入取款金额：'))
            r[username][1]=r[username][1]-m
            print('当前余额：',r[username][1])
            update()
        if chance=='5':
            exit()
def update():
    # print(type(r[username]))
    # r[username].append(money)
    with open("custominfo.json", "w+") as f:
        json.dump(r, f)

main()