# -*- coding: utf-8 -*-
"""
	元组拆包 --- 难点
"""
# 预先定义一个元组
tup9 = ('Python', 'Java', 'C++')

# print(f'原来的元组值是：',tup_9)
print('原来的元组值是',tup9)

# 复制为三个变量
Andy, yangmi , Tfboys  = tup9
print('元组拆包例子：')
print()
print('yangmi最喜欢的编程语言是:',yangmi)

# 如果个数与元组数不同，则出差
# Andy, yangmi  = tup9

# 嵌套元组也可以拆包
tup10 = 1, 2 ,('Python', 'Java')
print()

a, b,(Andy, yangmi) = tup10
print('a = ', a,'b=', b, 'Andy = ', Andy)

# 使用 _ 表示不想要的元组值
Andy, _ , Tfboys  = tup9
print('Andy = ', Andy)


# 使用星号 * 表示任意多个对象值 *rest
And, *rest = tup9
print()
print('Andy = ', Andy)

# *_也可以在多个变量中间

# 交换两个变量

Andy = 'Python'
Yanmgi ='C++'

print('交换前的：')
print('Andy = ',Andy, 'Yanmgi= ' ,Yanmgi)

Andy,Yanmgi = Yanmgi, Andy

print()
print('交换过的：')
print('Andy = ',Andy, 'Yanmgi= ' ,Yanmgi)

