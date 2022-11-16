# -*- coding: utf-8 -*-

"""
@author: Sword
@email: 173963781@qq.com
@file: h5.py
@time: 2022/11/16 9:31
"""

# 在Python中, 一个等号(=)和两个等号(==)的功能是一样的吗?
# 不一样, (=)表示赋值, (==)表示判断是否相等

# 请问下面代码为什么会报错?
"""
3  < = 4
SyntaxError: invalid syntax
"""
# 小于号和等于号中间不能有空格

# 请问下面代码返回的 True 还是 False?
"""
3 <= 5 >= 4
"""
# True

# 请问下面代码返回的值是什么?
"""
1 + 1 >= 2
"""
# True

# 请问下面代码存在什么问题
"""
if guess == 8:
    print("你是小甲鱼心里的蛔虫嘛？！")
   print("哼，猜中了也没奖励！")
else:
    print("猜错啦，小甲鱼现在心里想的是8！")
"""
# 缩进有问题

# 请问下面A、B、C、D四个表达式中，哪些将返回True？
"""
A. 'FishC' == '''FishC'''
B. "小甲鱼" == "小乌龟"
C. 520 == int(520.1314)
D. 9 == int(9.9)
"""
# A C D

if __name__ == '__main__':
    num1 = input("请输入第一个整数：")
    num2 = input("请输入第二个整数：")

    if num1 < num2:
        print("第一个数比第二个数小")

    if num1 > num2:
        print("第一个数比第二个数大")

    if num1 == num2:
        print("第一个数和第二个数一样大")
