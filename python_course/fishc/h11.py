# -*- coding: utf-8 -*-

"""
@author: Sword
@email: 173963781@qq.com
@file: h11.py
@time: 2022/12/3 15:21
"""

# 请问下面表达式的值是？
"""
>>> 3 == not 5
"""
# False
# 回答错误，由于 not 比 == 运算符低，所以会报错

# 请问下面表达式的值是？
"""
>>> 3 or 5 and 0
"""
# 3

# 请问下面表达式的值是？
"""
>>> 3 and 5 + True or False
"""
# 6

# 请问下面表达式的值是？
"""
>>> 0 and not 1 or not 2 and 3 or 4 and not 5
"""
# 0 and False or False and 3 or 4 and False
# 0 or False and 3 or 4 and False
# 0 or False or 4 and False
# 0 or False or 4
# 4
# 答题错误，4 and False 的结果应该是 False

# 请问下面表达式的值是？
"""
>>> 1 == 2 < 3
"""
# False

# 请将下面的链式比较转换为使用 and 的普通比较
"""
>>> 1 < 2 > 3 < 4 < 5
"""
# False
# 没读对题 1 < 2 and 2 >3 and 3 < 4 and 4 < 5

if __name__ == '__main__':
    # 有趣的数学题
    i = 1
    while True:
        if i % 2 == 1 and i % 3 == 2 and i % 5 == 4 and i % 6 ==5 and i % 7 == 0:
            break
        i += 1

    print("最终结果是：{}".format(i))
