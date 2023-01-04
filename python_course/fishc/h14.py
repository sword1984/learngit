# -*- coding: utf-8 -*-

"""
@author: Sword
@email: 173963781@qq.com
@file: h14.py
@time: 2022/12/7 9:04
"""
# Python 同一个代码块中的所有语句必须遵循什么原则？
# 统一缩进

# 请问下面代码是否能够正常执行？
"""
x = 3
y = 5
if x > y:
print("x比y大")
"""
# 不能正常执行，没有遵循同一个代码块中的统一缩进原则

# 请问下面代码是否能够正常执行？
"""
x = 3
y = 5
if x < y: print("x比y小")
"""
# 可以

# 请问下面代码是否能够正常执行？
"""
x = 3
y = 4
z = 5

if x < y:
  print(x, "<", y)
  if y < z:
            print(y, "<", z)
            print(x, "<", z)
"""
# 不能

# 请问下面代码是否能够正常运行？
"""
x = 3
y = 4
z = 5

if x < y:
  print(x, "<", y)
  if y < z:
            print(y, "<", z)
        print(x, "<", z)
"""
# 不能


if __name__ == '__main__':
    # 编写一个程序，让用户输入一个整数，判断其是否奇数还是偶数
    num = input("请输入一个整数：")

    if not num.isdigit():
        print("你输入的并不是一个整数，程序结束")
        exit()

    num = int(num)

    if num % 2:
        print("{}是一个奇数".format(num))
    else:
        print("{}是一个偶数".format(num))

    # 通常企业发放的年终奖是根据一年的盈利进行提成， A 公司的提成规则如下
    """
        当利润低于或等于 10 万元时：年终奖为 10%
        当利润高于 10 万元，低于 20 万元时：低于 10 万元的部分按 10% 提成，高于 10 万元的部分，按 7.5% 提成
        当利润 20 万到 40 万之间时：低于 10 万元的部分按 10% 提成，高于 10 万元低于 20 万元的部分，按 7.5% 提成，高于 20 万元的部分，按 5% 提成
        当利润 40 万到 60 万之间时：低于 10 万元的部分按 10% 提成；高于 10 万元低于 20 万元的部分，按 7.5% 提成；高于 20 万元低于 40 万元的部分，按 5% 提成；高于40万元的部分，按 3% 提成
        当利润 60 万到 100 万之间时：低于 10 万元的部分按 10% 提成；高于 10 万元低于 20 万元的部分，按 7.5% 提成；高于 20 万元低于 40 万元的部分，按 5% 提成；高于40万元低于 60 万元的部分，按 3% 提成；高于60万元的部分，按 1.5% 提成
        当利润高于 100 万元时：低于 10 万元的部分按 10% 提成；高于 10 万元低于 20 万元的部分，按 7.5% 提成；高于 20 万元低于 40 万元的部分，按 5% 提成；高于40万元低于 60 万元的部分，按 3% 提成；高于60万元低于 100 万的部分，按 1.5% 提成；超过 100 万元的部分按 1% 提成
    """
    # 请编写一个程序，根据录入的利润，计算出应该发放的奖金总数？
    profitability = int(input("请输入今年的利润："))
    prize = 0

    if profitability <= 100000:
        prize = profitability * 0.1
    elif profitability <= 200000:
        prize = 100000 * 0.1 + (profitability - 100000) * 0.075
    elif profitability <= 400000:
        prize = 100000 * 0.1 + 100000 * 0.075 + (profitability - 200000) * 0.05
    elif profitability <= 600000:
        prize = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.5 + (profitability - 400000) * 0.03
    elif profitability <= 1000000:
        prize = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.5 + 200000 * 0.03 + (profitability - 600000) * 0.015
    elif profitability > 1000000:
        prize = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.5 + 200000 * 0.03 + 400000 * 0.015 + (
                    profitability - 1000000) * 0.01

    print("应该发放的奖金总数是：{}".format(prize))
