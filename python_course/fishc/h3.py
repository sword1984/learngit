# -*- coding: utf-8 -*-

"""
@author: Sword
@email: 173963781@qq.com
@file: h3.py
@time: 2022/11/15 11:39
"""

# 哪个变量名不正确？为什么？(A) MM_520  (B)_MM520_  (C)520_MM  (D)_520_MM  (E)我M爱M你
# C，因为变量不能以数字开头

# 你觉得下面代码出错的原因是什么?
"""
Traceback (most recent call last):
  File "C:\\Users\Legion\PycharmProjects\learngit\python_course\fishc\h3.py", line 17, in <module>
    print(x)
          ^
NameError: name 'x' is not defined
"""
# 因为变量x没被初始化

# 你觉得下面代码中，print()函数会打印什么内容
"""
x = 520
x = 880
print(X)
"""
# 880
# 没注意这个X是大写的，所以会报错

# 你觉得下面代码中，print()函数会打印什么内容？
"""
x, y, z = 3, 4, 5
x, y, z = y, x, z
print(x, y, z)
"""
# 4, 3, 5

# 你觉得下面代码中，print()函数会打印什么内容？
"""
print("小甲鱼常说："Good good study, day day up!"")
"""
# 会报错

# 按要求打印字符串
print("Bruce Eckel say:\"Life is short, let's learn Python")

if __name__ == '__main__':
    # 编写代码，计算一年有多少秒
    dpy, hpd, mph, spm = 365, 24, 60, 60
    spy = dpy * hpd * mph * spm
    print(spy)

    # 编写代码，使用 input() 函数让用户录入姓名
    name = input("请输入您的名字：")
    print("你好，{}！".format(name))
