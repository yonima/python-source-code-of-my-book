# -*- coding: utf-8 -*-
"""
 使用列表解决参数个数未知的情况
"""


# 使用默认值，以及任意数量的实际参数
def welcome_beijing(*name, question='您最想去哪里玩？'):
	print('任意数量参数的类型是：', type(name))
	print(name)
	for name_single in name:
		print(type(name_single))
		print(f'{name_single}, 北京欢迎你！{question}')
		

# 定义人员列表
list_name = ['刘德华', '杨幂', 'Tfboy', '吴谨言']

# 使用列表传递参数
welcome_beijing(list_name)

# 实参前面一定要有 *
welcome_beijing(*list_name)

print(tuple(list_name))