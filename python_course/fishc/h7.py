# -*- coding: utf-8 -*-

"""
@author: Sword
@email: 173963781@qq.com
@file: h7.py
@time: 2022/11/22 15:45
"""

# "所有使用算法生成的随机数，都是伪随机数！"这种说法对吗?
# 对

# 如果要使用 random 模块，第一步应该怎么做？
# 导入模块 import random

# 调用 random.randint(1, 10) 函数生成一个随机数，是否有可能会出现 10 这个数
# 可能

# 下面这句代码的作用是什么
"""
random.choice("ilovefishc")
"""
# 在 "ilovefishc" 字符串随机选取一个字母

# 请问下面两个 print() 语句打印的结果是否相同，为什么
"""
    import random

    random.seed(1)
    print(random.randint(1, 10), random.randint(1, 100), random.randint(1, 1000))

    random.seed(1)
    print(random.randint(1, 10), random.randint(1, 100), random.randint(1, 1000))

"""
# 相同

if __name__ == "__main__":
    # 用 random ，在0~99之间随机抽取一个偶数
    import random

    print("从0~99之间随机抽取一个偶数：{}".format(random.randrange(0, 99, 2)))

    # 编写一个双色球的开奖模拟程序

    print("开奖结果是：{}".format(" ".join(map(str, random.sample(population=range(1, 33), k=6)))))
    print("特别号码是：{}".format(random.randrange(1, 16)))