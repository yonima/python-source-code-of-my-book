# -*- coding: utf-8 -*-
"""
	列表基本操作知识点（五大基本操作）：
		1、访问列表元素

		2、 添加列表元素
		
		2、补充知识点：从空列表构建新列表
		
		3、修改列表元素
		
		4、删除列表元素

		5、列表排序及其他
"""

# 定义列表 -- Python实战圈成员列表
names_python_pc = ['陈升','刘德华','杨幂','TFboys']


'''
	1、访问列表元素
'''
# 根据索引访问列表元素--访问杨幂
yangmi = names_python_pc[2]
print('Python实战圈成员列表种第三个是：',yangmi)

# 两种方法访问最后一个元素
print()
first_last = names_python_pc[-1]
print('第一种方法获取最后一个元素',first_last)

second_last = names_python_pc[3]
print('第二种方法获取最后一个元素',first_last)
'''
	2、 添加列表元素
'''
# 第一种方法 insert(index,x)
print()
names_python_pc.insert(0, '魏璎珞')
print(f'插入新元素后的列表是：{names_python_pc}')

# 第二种方法：append(x)
names_python_pc.append('傅恒')
print(f'第二种方法插入新元素后的列表是：{names_python_pc}')
'''
	2、补充知识点：从空列表构建新列表
'''
# 构建空的列表 [ ]
yan_xi_gong_luo = [ ]

# 为空的列表动态添加元素
yan_xi_gong_luo.append('魏璎珞')
yan_xi_gong_luo.append('皇后')
yan_xi_gong_luo.append('纯妃')

print('构建空的列表 [ ]: ',yan_xi_gong_luo)

'''
	3、 修改列表元素
'''
# 根据索引修改列表元素
print()
print('修改前的列表元素：',names_python_pc)
names_python_pc[2] = '扶摇'
print('修改后的列表元素：',names_python_pc)

'''
	4、删除列表元素
'''
print()
# 第一种方法删除  del pop
del names_python_pc[0]
print('del删除元素后的列表元素有：',names_python_pc)

# 根据位置信息删除
print()
pop_name = names_python_pc.pop()
print(pop_name)

print()
pop_name_1 = names_python_pc.pop(1)
print(f'根据位置信息删除: {pop_name_1}')

print('删除后的列表元素有：',names_python_pc)


# 第二种方法删除 remove('值')
print()
names_python_pc.remove('TFboys')
print('remove 删除后的列表元素有：',names_python_pc)


'''
	5、列表排序及其他
'''
# 构建列表
list_1 = ['p','f','b','a','d','e','f','g']

# 复制列表copy()
list_2 = list_1.copy()
print()
print('5、列表排序及其他')
print()
print('复制列表：',list_2)

# 统计列表中f出现的次数 count()
print('统计列表中 f 出现的次数', list_1.count('f'))
print('统计列表中 b 出现的次数', list_1.count('b'))

# 找出某一个元素的位置信息 index
print('查找 b 元素所在的位置：', list_1.index('b'))

# print('B所在的位置', )

# 颠倒顺序 reverse()
print('原来的元素顺序:', list_1)
list_1.reverse()
print('颠倒后的元素顺序:', list_1)

'''
	排序
'''
print()
print('5.1 、列表排序')
print()
# 永久顺序
list_1.sort()
print(' sort  :', list_1)

# 降序
list_1.sort(reverse=True)

print('降序排列元素', list_1)

# len
print()
print('list_1长度为:' , len(list_1))

print()

# 临时排序  sorted()

temp_list = sorted(list_1)

print('临时排序', temp_list)
print('原来的列表元素顺序',list_1)
