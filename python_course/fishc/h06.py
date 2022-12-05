# -*- coding: utf-8 -*-

"""
@author: Sword
@email: 173963781@qq.com
@file: h06.py
@time: 2022/11/17 21:52
"""

# 请问下面的代码是打印“YES”还是“NO”？
"""
if 'FishC' == "fishc":
    print("YES")
else:
    print("NO")
"""
# NO

# 请问下面代码会打印多少个”Yo~“?
"""
yoo = 222
while yoo < 233:
    print("Yo~")
"""
# 一直打印

# 请问下面代码存在什么问题？
"""
age = input("请输入你的年龄：")

if age <= 18:
    print("你已经成年^o^")
else:
    print("对不起，你还未成年T_T")
"""
# 输入的内容是字符串，要用int函数转换成数字

# 下面代码是一个死循环，请添加一个语句，使其打印一遍后退出循环
"""
while True:
    print("iloveFishC.com")
"""
# break

# 请阅读下面代码，根据你的理解，代码中的问号（？？？）处应该填写什么内容？
"""
x = input("请输入一个数字：")
x = int(x)

if x >= 20:
    print("大于等于20")
else:
    if x <= 10:
        print("小于等于10")
    else:
        print("？？？")
"""
# 大于10小于20

if __name__ == "__main__":
    # 编写一个成绩评级程序，要求用户输入分数，程序返回对应的评级。
    """
    分数 < 60，D
    60 <= 分数 < 80，C
    80 <= 分数 < 90，B
    90 <= 分数 < 100，A
    分数 == 100，S
    """

    score = int(input("请输入你的分数："))

    if score == 100:
        print("S")
    if 90 <= score < 100:
        print("A")
    if 80 <= score < 90:
        print("B")
    if 60 <= score < 80:
        print("C")
    if score < 60:
        print("D")

    # 修改上一题的代码，让程序可以不断接收输入，直至用户输入小写字母 e 结束程序
    while True:
        score = input("请输入你的分数：")
        if score == "e":
            break
        else:
            score = int(score)

        if score == 100:
            print("S")
        if 90 <= score < 100:
            print("A")
        if 80 <= score < 90:
            print("B")
        if 60 <= score < 80:
            print("C")
        if score < 60:
            print("D")
