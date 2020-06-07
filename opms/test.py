#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2020/06/03 10:42:53
@Author  :   YLw 
@Version :   1.0
@Contact :   924478750@qq.com
'''
# Start typing your code from here

'''def a():
    '这是文档字符串'
    pass

print(a.__doc__)
'''


from matplotlib import pyplot as plt 
x =  [5,8,10] 
y =  [12,16,6] 
x2 =  [6,9,11] 
y2 =  [6,15,7] 
plt.bar(x, y, align =  'center') 
plt.bar(x2, y2, color =  'g', align =  'center') 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis') 
plt.show()


