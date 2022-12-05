# -*- coding: utf-8 -*-

"""
@author: Sword
@email: 173963781@qq.com
@file: h12.py
@time: 2022/12/4 20:47
"""

if __name__ == '__main__':
    n = int(input("请输入三角形的层数："))

    i = 1
    while i <= n:
        j = 0
        while j < n-i:
            print(" ", end="")
            j = j + 1

        j = 0
        while j < 2 * i - 1:
            print("*", end="")
            j = j + 1

        print("")
        i = i + 1

    num = int(input("请输入一个整数："))

    if num % 2 == 0 and num % 3 == 0:
        print("{}能被 2 和 3 同时整除".format(num))
    else:
        print("{}不能被 2 和 3 同时整除".format(num))

    if num % 2 == 0:
        print("{}能被 2 整除".format(num))
    else:
        print("{}不能被 2 整除".format(num))

    if num % 3 == 0:
        print("{}能被 3 整除".format(num))
    else:
        print("{}不能被 3 整除".format(num))

    if (num % 2) and (num % 3):
        print("{}不能被 2 和 3 同时整除".format(num))
