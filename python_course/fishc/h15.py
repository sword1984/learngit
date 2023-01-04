# -*- coding: utf-8 -*-

"""
@author: Sword
@email: 173963781@qq.com
@file: h15.py
@time: 2022/12/11 11:15
"""
# python 是如何区分不同代码块的呢?
# 缩进

# 请问下面代码执行后， x 变量的值是多少?
"""
x = 520 if "Love" else 404
"""
# 520

# 请将下面代码中的条件分支部分修改为使用条件表达式来实现：
"""
age = 18
isMale = True
if age < 18:
    print("抱歉，未满18岁禁止访问。")
else:
    if isMale:
        print("任君选购！")
    else:
        print("抱歉，本店商品可能不适合小公举哦~")
"""
age = 18
isMale = True
(print("抱歉，未满18岁禁止访问。") if age < 18 else
 print("任君选购！") if isMale else print("抱歉，本店商品可能不适合小公举哦~"))

# 其实，大多数 if - else 条件分支还可以使用 and - or 运算符组合的表达式来代替，那么如果将下面代码转变成 and - or 业实现，应该是怎样的呢？
"""
if "Love":
    520
else:
    404
"""
# "Love" and True 520
# "Love" and False 404

# 请将下面的条件分支语句，使用条件表达式实现，并尝试理解 这段代码的目的是什么
"""
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)
"""
a, b, c = 1, 2, 3
(
    print(a) if a < c else print(b) if a < b else
    print(b) if b < c else print(c)
)
# 找出 a, b, c 最小的一个

if __name__ == '__main__':
    """
    请编写一个程序，根据录入的血液酒精含量来判断是否酒驾？

    当酒精含量小于 20 毫克时：不构成饮酒行为
    当酒精含量大于等于 20 毫克且 小于 80 毫克时：已经达到酒后驾驶的标准
    当酒精含量大于等于 80 毫克时：已经达到醉酒驾驶的标准
    
    
    要求：请先画出程序流程图，再用代码实现。
    """
    alcohol = int(input("请输入血液酒精含量："))

    if alcohol < 20:
        print("不构成饮酒行为")
    elif alcohol < 80:
        print("已经达到酒后驾驶的标准")
    else:
        print("已经达到醉酒驾驶的标准")

    # 验证角谷猜想
    num = int(input('请输入一个自然数: '))
    while True:
        if num == 1:
            break
        elif num % 2:
            print('{}*3+1={}'.format(num, num * 3 + 1))
            num = num * 3 + 1
        else:
            print('{}/2={}'.format(num, num // 2))
            num = num // 2
