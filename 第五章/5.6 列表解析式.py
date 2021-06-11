# -*- coding: utf-8 -*-
"""
	列表解析式：
	1、指定条件的列表解析式: if  if--else 两种
	2、无条件列表解析式
	3、嵌套for循环列表解析式
"""
'''
1、指定 if 条件的列表解析式
'''
# 需求：求10以内的奇数
odds = []

# 使用range(10)生成数字
for n in range(10):
	# 如果数字除以2的余数为 1 则为奇数
	if n % 2 == 1:
		odds.append(n)
print(f'使用 for 循环求10以内的奇数有： {odds}')

'''
     把上面的代码转化为列表解析式的步骤为：
     1、复制 odds= []
     2、把 append 方法中的变量n写入新列表中，也就是odds = [n]
     3、复制 for 循环语句，注意不需要最后的冒号。也就是odds = [n for n in range(11)]
     4、复制 if 条件控制语句，注意也不需要最后的冒号。也就是odds = [n for n in range(11) if n % 2 ==1]

'''
odds = [n for n in range(10) if n % 2 == 1]
print('\n使用列表解析式：')
print(odds)

# python支持在括号之间断行，为了可读性。
odds = [
	n
	for n in range(10)
	if n % 2 == 1
]
print(f'\npython支持在括号之间断行{odds}')

'''
1、有 if -- else条件列表解析式
'''
# 10以内的奇数，并且把偶数加 1 变成奇数
print()

odds = []
for n in range(10):
	if n % 2 == 1:
		odds.append(n)
	else:
		odds.append(n + 1)
print('10以内的奇数，并且把偶数加 1 变成奇数', odds)

'''
    把上述代码变成列表解析式步骤：
    1、复制 odds= []
    2、把 append 方法中的变量n写入新列表中，也就是odds = [n]
    3、复制 if 语句，注意if写在for前面要求必须有else项 ，也就是 odds = [n if n % 2 ==1 ]
    4、复制 else 语句，也就是 odds = [n if n % 2 ==1 else n+1 ]
    5、复制 for 循环, 也就是 odds = [n if n % 2 ==1 else n+1 for n in range(10)]

'''
print()
odds = [n if n % 2 == 1 else n + 1 for n in range(10)]
print('\n使用if --else 列表解析式：')
print(odds)

# 为了可读性，对其段行
odds = [
	n
	if n % 2 == 1
	else n + 1
	for n in range(10)
]
'''
项目实战例子：把浮点数变成整数类型

    当数据分析时，我们经常遇到浮点类型的数据。这不便与以后的分析。
    我们使用列表解析式把浮点数变成整数类型。
    首先，我们把数据作用于if条件判断类型是不是浮点数。
    如果是，则把数据进行强制类型转换int()，否则直接放在列表中；
    
'''
data = ['Nelson', '2018-10-31', 320.0, 78.0, 1200.0, 3.0, 78.0, 'CN', 1400.0]
int_data = [int(x) if type(x) == float else x for x in data]
# 作业：请先写出FOR循环，然后按照复制黏体的方法写出列表解析式
print(f'\n把浮点数变成整数类型:{int_data}')

########################################
# 需求2
# 为了说明if结构的列表解析式，我们选取的例子是从一堆浮点数中选择大于1000的数据。
# 此时if条件就是筛选数据是否满足条件，如果满足则放入列表，否则放弃。
########################################
# 作业：请先写出FOR循环，然后按照复制黏体的方法写出列表解析式
data_1000 = [n for n in data if type(n)== float and n > 1000]
print(f'大于1000的数据:{data_1000}')

'''
2、无条件列表解析式
   需求：生成10个数字的列表
'''
print()
# 生成10个数字的列表
ten_list = []

# 使用range(11)生成10个数
for n in range(10):
    ten_list.append(n)
print(f'使用 for 循环生成10个数字的列表有： {ten_list}')

'''
     把上面的代码转化为列表解析式的步骤为：
     1、复制 ten_list= []
     2、把 append 方法中的变量n写入新列表中，也就是ten_list = [n]
     3、复制 for 循环语句，注意不需要最后的冒号。也就是ten_list = [n for n in range(11)]

'''
ten_list = [n for n in range(10)]
print(f'\n使用列表解析式的方法生成10个数字的列表：{ten_list}')

'''
3、嵌套for循环列表解析式
    需求：两个列表中同时为奇数的和
'''

print()
number_1 = [1, 2, 3]
number_2 = [4, 5, 6]
sum_odd = []
for i in number_1:
	for j in number_2:
		if i % 2 == 1 and j % 2 == 1:
			sum_odd.append(i + j)
print('两个列表中同时为奇数的和:', sum_odd)

'''
     把上面的代码转化为列表解析式的步骤为：
     1、复制 sum_odd = []
     2、把 append 方法中的变量 i + j 写入新列表中，也就是 sum_odd = [i+j]
     3、复制外层 for 循环语句，注意不需要最后的冒号。也就是 sum_odd = [i+j for i in number_1]
     4、复制内层 for 循环语句，注意不需要最后的冒号。也就是 sum_odd = [i+j for i in number_1 for j in number_2 】
     5、复制 if 语句，注意不需要最后的冒号。也就是 sum_odd = [i+j for i in number_1 for j in number_2 if i % 2 == 1 and j % 2 == 1]

'''
sum_odd = [i + j for i in number_1 for j in number_2 if i % 2 == 1 and j % 2 == 1]
print(f'列表解析式求两个列表中同时为奇数的和：{sum_odd}')

# 为了可读性，断行列表解析式


'''
作业：列表解析式生成九九乘法表
'''

# list_number = [print(f'{i} *{j} = {i *j}', end=' ') for i in range(1,10) for j in range(1,i+1)]
# print(list_number)
