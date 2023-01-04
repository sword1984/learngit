# -*- coding: utf-8 -*-

"""
@author: Sword
@email: 173963781@qq.com
@file: h17.py
@time: 2022/12/28 15:31
"""

# continue 语句和 break 语句都能够跳出循环体，那么它们的区别是什么呢？
# continue 是跳过循环体下面部分，break是跳出当前循环体

# 在不上机的情况下，你能看出下面代码会打印多少次 "FishC" 吗？j
"""
>>> i = 0
>>> j = 9
>>> while i < j:
...     i += 1
...     j -= 1
...     print("FishC")
"""
# 5

# 你觉得 while-else 语法存在的意义是什么？
# 判断while语句是否正常执行完毕

# 你能看出下面代码存在什么问题吗？
"""
>>> i = 0
>>> while i < 10:
...     if i % 2 == 0:
...         continue
...     i += 1
...     print(i)
"""
# 会陷入死循环

# 请看下面代码，当 break 语句执行之后，程序是跳转到位置 1 还是位置 2 呢？
"""
>>> day = 1
>>> while day <= 7:
>>>     while hour <= 8:
...         print("今天，我一定要坚持学习8个小时！")
...         hour += 1
...         if hour > 1:
...             break
...     # 位置1
...     day += 1
... # 位置2
"""
# 位置1

# 下面代码存在两个问题，细心的你发现了吗？
"""
>>> while True:
...     command = input("请输入命令（exit/pow）：")
...     if command == "pow":
...         base = input("请输入底数：")
...         exp = input("请输入指数：")
...         pow(base, exp)
...     elif command == "exit":
...         continue
"""
# 不应该使用continue，这样会陷入死循环，应该使用break

if __name__ == '__main__':
    # 将九九乘法表倒过来打印
    i = 9
    j = 1

    while j <= i:
        while j <= i:
            print('{}*{}={}'.format(i, j, i * j), end='  ')
            i -= 1
        i = 9
        j += 1
        print()

    #  找出 10 以内的所有素数，如果不是素数，请打印出该合数对应的乘积公式
    for i in range(2, 10):
        j = 2
        while j < i:
            if i % j == 0:
                print('{}={}*{}'.format(i, j, i//j))
                break
            j += 1
        else:
            print('{}是一个素数。'.format(i))
