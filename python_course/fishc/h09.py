# -*- coding: utf-8 -*-

"""
@author: Sword
@email: 173963781@qq.com
@file: h09.py
@time: 2022/12/2 11:26
"""

# 请问 1 + 2 / 3 跟 1 + 2 // 3 的结果有何不同
# 结果不同，结果类型不同

# 无论是真除法 (/) 还是地坂除 (//)，都需要注意的一个问题是什么？
# 除数不能为零

# 请问 1 + -2 - +3 / +5，计算结果是？
# -1.6

# pow(3, 4, 5)的含义是什么？
# 3的4次方，得到的结果再地板除5

# (x // y) * y + (x % y)的结果是什么？
# x

# 单纯使用 int() 函数，不借助其它函数实现"四舍五入"的方式来取整
# x = int(x + 0.5)

if __name__ == '__main__':
    # 计算 1000000 以内所有偶数的和
    result = 0
    for i in range(1, 1000001):
        if i % 2 == 0:
            result += i

    print("1000000 以内所有偶数的和是：{}".format(result))

    # 计算舍罕王需要的麦子数量
    total = 0
    i = 1

    while i <= 64:
        wheats = pow(2, i-1)
            total += wheats
            i += 1

    print("舍罕王应该给达依尔 {} 粒麦子！".format(total))