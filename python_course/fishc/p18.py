# -*- coding: utf-8 -*-

"""
@author: Sword
@email: 173963781@qq.com
@file: p18.py
@time: 2023/1/4 16:38
"""

if __name__ == "__main__":
    i = 1

    while i <= 9:
        j = 1
        while j <= i:
            print('{} * {} = {}'.format(j, i, j*i).ljust(13, ' '), end='')
            j += 1
        i += 1
        print()
