"""
    整数四则运算知识点
    1、四则运算
    2、format方法
    3、方法与函数的区别
"""
'''
    第一个四则运算
'''
# 加法
add = 3 + 5
print(add)

# 减法
sub = 10 - 8
print(sub)
print('求 10 - 8 的差是：', sub)


sub = 9 -2
print('求 9 - 2 的差是：', sub)

# 乘法
print()
multi = 3 * 7
print('求 3 * 7的 结果是{}'.format(multi))

# 除
div = 10 /2
print(div)

# 取模运算：返回除法的余数
delivery = 7 % 3
print('求 7 % 3 的结果是：{}'.format(delivery))

# 取整除，返回商的整数
round_number = 7 // 3
print('求7 // 3的结果是：{}'.format(round_number))

# 幂运算
power = 7 ** 3
print('求7 ** 3 的结果是{}'.format(power))

'''
    第二个： format()方法是格式化输出，也就是在{}的地方替换为变量的值
    后面几天的内容中，它会被经常用到
'''
print()
sub = 9 - 2
print('求 9 - 2 的差是：', sub)

sub_1 = 9
sub_2 = 2
sub = sub_1 - sub_2
print('求 {} - {} 的差是：{}'.format(sub_1, sub_2, sub))

'''
    方法与函数的区别：
    1、方法是需要调用才可以使用；函数可以直接使用
    2、方法是面向对象的概念；函数是面向过程的概念。第七天内容介绍
'''