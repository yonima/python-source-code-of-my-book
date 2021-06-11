# -*- coding: utf-8 -*-
"""
for 循环结构

1、For循环的定义
2、列表与 for 循环
3、字典与 for 循环
4、嵌套 for 循环

"""
'''
遍历字符串

需求： 计算 Now is better than never' 中 e 出现的次数
'''
str_data = 'Now is better than never'
count = 0 # 计数器

for count_e in str_data:
	if count_e == 'e':
	    count += 1
		
print(f'计算 Now is better than never 中 e 出现的次数{count}')

# 另外一个方法
count_e = str_data.count('e')
print(f'\n计算 Now is better than never 中 e 出现的次数{count_e}')
'''
列表与 for 循环
'''
# 1、 动态创建列表：需求：求10以内的奇数

odd = []
for n in range(10):
	if n % 2 == 1:
		odd.append(n)
print('动态创建列表：需求：求10以内的奇数', odd)

	
# 作业：动态创建列表：需求：求10以内的偶数

# 2、遍历列表：请输出 XX是《扶摇》电视剧的人物，比如 扶摇是《扶摇》电视剧的人物。
name_fuyao = ['扶摇','周叔','国公','无级太子','医圣','非烟殿主','穹苍']
print('输出列表元素:', name_fuyao)

for name in name_fuyao:
	print(f'\n\t{name} 是《扶摇》电视剧的人物， ')

'''
字典与 for 循环
'''
# 构建一个字典，记录各宫嫔妃的年薪银子，单位是两
name_dictionary = {'妃子': 300,
                   '皇后': 1000,
                   '皇贵妃': 800,
                   '贵妃': 600,
                   '斌': 200}
# 使用for()循环遍历字典中的key-value,方法items()返回键值对列表
'''
需求：
1、 请输出 各个级别的嫔妃的年薪是: 比如 妃子 的年薪是 300 两
2、 请输出 后宫嫔妃的级别有
3、 请输出 后宫嫔妃的年薪有以下结构组成：
'''
print('各个级别的嫔妃的年薪是', name_dictionary.items())

print('各个级别的嫔妃的年薪是:')
for name, value in name_dictionary.items():
	print(f'\t{name} 的年薪是 {value} 两')

print('后宫嫔妃的级别有:')
for name in name_dictionary.keys() :
	print(name)
	
# 作业：请输出 后宫嫔妃的年薪有以下结构组成：

'''
嵌套 for 循环
需求：请实现下面的图像

*******
*******
*******
*******
'''
print()
for row in range(4):
	for col in range(7):
		print('*', end='')
	print()

'''
*
***
*****
*******
'''
