# -*- coding: utf-8 -*-

"""
@author: Sword
@email: 173963781@qq.com
@file: h2.py
@time: 2022/11/15 11:02
"""

# IDLE的交互模式和编辑模式有什么区别？
# 交互模式每一行命令就立马执行，编辑模式可以保存

# 在课堂上敲的代码中，除了 print() 和 input() 你觉得还有哪一个是 Python 的 BIF 内置函数？
# int()

# 请问 print() 和 Print() 的功能一样吗？
# 不一样，因为 Python 是区分大小写的

# 请统计一下 Python 一共有多少个 BIF 内置函数？
# len(dir(__builtins__)) 共 159 个

if __name__ == '__main__':
    # 计算一年有多少秒
    print("一年有{}秒".format(365 * 24 * 60 * 60))

    score = int(input("这次数学考试成绩："))
    if score == 100:
        print("好棒，你离女神又近了一步^_^")
    else:
        print("小子，想要幸福，就得努力!")

    print("游戏结束，不玩了^_^")
