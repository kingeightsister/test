#coding=utf-8
val=int(input('>>>'))
for i in range(val):
    if i==0 or i==(val-1):
        print('*'*val)
    else:
        print('*'+' '*(val-2)+'*')