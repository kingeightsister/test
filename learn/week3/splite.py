#coding=utf-8

# a='I am very very sorry'
# x=a.startswith('I')字符串以xx开始和结尾，返回布尔值
# x=a.endswith('sorry',3,5)
# x=a.find('am')==2查找是否在对应下标位置处
# x=a.find('a',1,3)==2
# print(x)

#字符串格式化，%S等与后面赋值需一一对应
#%d,%s,%u,%# 等代表不同类型的占位符
# x='i am %s %s'%(20,30)
# x='%#x'% 10
# print(x)

#format位置参数
# x='{}:{}'.format('192.189.109.22',8888)
# print(x)
#format关键字参数或命名参数
# s='{server}{1}:{0}'.format(8888,'192.189.109.22',server='web server info:\n')
# print(s)
#访问元素
# n='{0[0]}.{0[1]}'.format(('rachel','com'))
# print(n)
#对象属性访问
# from collections import namedtuple
# Point =namedtuple('Point','x y')
# p1=Point(4,78)
# print(p1)
# m='{{{0.x},{0.y}}}'.format(p1)
# print(m)
# x='{:*^30}'.format(6)
# x='{:^30}'.format('centered')
# print(x)

#输入一个正整数，判断是几位数，打印每一位数字及其重复的次数，依次打印个十百千万位
x=input('请输入一个正整数:')
n=x.lstrip(' 0').rstrip() #右边的0不计算不遍历
l={}
a=len(n)
for i in range(a):
    print(n[i])
    if n[i] not in l:
        l[n[i]]=1
    else:
        l[n[i]]+=1
print("这个数是{}位数，数字出现的次数是{}".format(a,l))



'''老师的版本'''
# lst=input('>>>').strip().lstrip('0')
# length=len(lst)
# for i in range(length):
#
#     print(i,a.count(i))
# c=(','.join(b)).split(',')
# c.reverse()
# print(c)



#输入5个数字，打印每个数字的位数，将这些数字排序打印，要求升序打印
# l=[]
# for i in range(5):
#     m=input('>>>')
#     print('这个数是{}位数'.format(len(m)))
#     l.append(int(m))
# l.sort()
# print(l)