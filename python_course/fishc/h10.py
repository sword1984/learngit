# -*- coding: utf-8 -*-

"""
@author: Sword
@email: 173963781@qq.com
@file: h10.py
@time: 2022/12/3 11:32
"""

# 请问 python 是否支持链式比较？
# 支持

# 请问下面两段代码有什么区别？
"""
>>> if bool(250):
...     print("Yeah, you are right.")


>>> if 250:
...     print("Yeah, you are right.")
"""
# 结果没区别

# 在 python 中，所有的对象都可以进行真值检测，对吗？
# 对

# 请问下面表达式的值是？
"""
>>> not 3 == 5
"""
# True

# 在 python 中，True 和 False 两个关键字是完全等值1 和 0的，对吗？
# 不对

# 请问下面代码打印的内容是什么？
"""
>>> print(5 > 3 and 4)
"""
# 4

# 请问下面代码打印的内容是什么？
"""
>>> from fractions import Fraction
>>> print(Fraction(1, 2) * 2)
"""
# 1

if __name__ == '__main__':
    # 判断给定年份是否是闰年
    year = int(input("请输入一个年份："))

    if not year % 400:
        print("{} 是闰年".format(year))
    else:
        if not year % 4 and year % 100:
            print("{} 是闰年".format(year))
        else:
            print("{} 不是闰年".format(year))
