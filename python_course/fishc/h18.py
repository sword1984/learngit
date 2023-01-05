# -*- coding: utf-8 -*-

"""
@author: Sword
@email: 173963781@qq.com
@file: h18.py
@time: 2023/1/4 17:19
"""

# 请问下面代码打印的结果是什么?
"""
>>> for i in range(10):
...     print(i, end=' ')
...     i = 5
"""
# 0123456789

# 请问下面代码打印结果是什么？
"""
>>> a, b, c = range(3, 10, 3)
>>> print(a + b + c)
"""
# print(3 + 6 + 9)

# 请问下面代码打印的结果是什么？
"""
>>> len(range(0, 10, 2))
"""
# 5

# 请问下面代码打印的结果是什么？
"""
>>> len("FishC") + len(110)
"""
# 报错，整数不能使用 len 函数

# 请问下面代码执行后，result 变量的值是多少？
"""
>>> result = 0
>>> for each in range(-10, -100, -20):
...     result += each
"""
# -10 + -30 + -50 + -70 + -90 = -250

# 请问下图中，空行位置应该填写什么代码，程序才能如期执行？
"""
for num in range(2, 10:
    if num % 2 == 0:
        print(num, '是偶数。')
        
    print(num, '是奇数。')
"""
# num += 1

if __name__ == "__main__":
    # 编写一个程序，求解 100~999 之间的水仙花数。
    num = 100
    while num < 1000:
        gewei = num % 10
        shiwei = (num // 10) % 10
        baiwei = num // 100

        if (gewei ** 3) + (shiwei ** 3) + (baiwei ** 3) == num:
            print(num)

        num += 1

    # 判断一个整数是否为回文数
    x = int(input("请输入一个正整数："))

    if x < 0 or (x % 10 == 0 and x != 0):
        print("不是回文数。")
    else:
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10

        if x == revertedNumber or x == revertedNumber // 10:
            print("是回文数。")
        else:
            print("不是回文数。")


