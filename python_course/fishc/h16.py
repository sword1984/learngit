# -*- coding: utf-8 -*-

"""
@author: Sword
@email: 173963781@qq.com
@file: h16.py
@time: 2022/12/28 9:55
"""

# 请问下面代码存在什么问题？
"""
love = 'yes'
while love = 'yes':
    love = input("今天你还爱我吗：")
"""
# 判断语句应该用 ==, =是赋值符号

# 如果不上机，你能算出下面循环执行完毕之后，打印的值应该是多少吗？
"""
i = 1
sum = 0
while i < 10:
    sum = sum + i
    i = i + 1
print(sum)
"""
# 45

# 请问下面代码是否会构成一个死循环？
"""
x = 9
while x:
    print(x)
    x -= 3
    x += 1
"""
# 只有当x为0的时候才会退出循环，而x-3+1相当于x-2, 9-2-2-2-2-2，相当于1-2，等于-1，永远不会为0就是死循环

# 当程序跑起来之后，如果发现是死循环，如何强制退出？
# ctrl+c

# 以下两段代码实现相同的功能，你觉得哪一段代码的实现更优雅？
"""
代码A:
password = ''
while password != "FishC":
    password = input("请输入密码：")
    
print("欢迎您来！")


代码B:
while True:
    password = input("请输入密码：")
    if password == "FishC":
        break
    
print("欢迎您来！")
"""
# 感觉差不多吧

if __name__ == '__main__':
    # 请编写一个程序
    while True:
        sentence = input('请输入一个句口号（输入 STOP 结束）：')
        if sentence == 'STOP':
            break

    # 如果抛硬币的次数小于 100，则打印每次的结果，否则不打印
    # 统计最终正面和反面的次数
    import random

    count = int(input('请输入抛硬币的数数：'))
    coin = ['正面', '反面']
    front = reverse = 0

    isprint = True if count < 100 else False

    while count:
        temp = random.choice(coin)
        if temp == '正面':
            front += 1
        else:
            reverse += 1

        if isprint:
            print(temp, end=' ')

        count -= 1

    print('\n一共模拟了 {} 次抛硬币, 结果如下：'.format(front + reverse))
    print('正面：{}次'.format(front))
    print('反面：{}次'.format(reverse))

    # 让程序分别统计正反面最多出现连续的次数
    import random

    count = int(input('请输入抛硬币的数数：'))
    coin = ['正面', '反面']
    front = reverse = 0
    front_count = reverse_count = 0
    front_max = reverse_max = 0
    side_last = ''

    isprint = True if count < 100 else False

    while count:
        temp = random.choice(coin)
        if temp == '正面':
            front += 1
        else:
            reverse += 1

        if temp == side_last:
            if temp == '正面':
                front_count += 1
                if front_count > front_max:
                    front_max = front_count

            if temp == '反面':
                reverse_count += 1
                if reverse_count > reverse_max:
                    reverse_max = reverse_count
        else:
            side_last = temp
            if side_last == '正面':
                front_count = 1
                reverse_count = 0
            if side_last == '反面':
                reverse_count = 1
                front_count = 0

        if isprint:
            print(temp, end=' ')

        count -= 1

    print('\n一共模拟了 {} 次抛硬币, 结果如下：'.format(front + reverse))
    print('正面：{}次'.format(front))
    print('反面：{}次'.format(reverse))
    print('最多连续正面：{}次'.format(front_max))
    print('最多连续反面：{}次'.format(reverse_max))
