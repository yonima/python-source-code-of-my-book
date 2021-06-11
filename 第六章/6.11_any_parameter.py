# -*- coding: utf-8 -*-
"""
任意数量的实参:*name
需求：
	刘德华，北京欢迎你！您最想去哪里玩？
	杨幂，北京欢迎你！您最新想去哪里玩？
	小码哥，北京欢迎你！您最想去哪里玩？
"""


# 使用默认值，以及任意数量的实际参数
def welcome_beijing(*name , question='您最想去哪里玩？'):
	"""
	使用默认值，以及任意数量的实际参数
	:param name:
	:param question:
	:return:
	"""
	# 元组
	print('查看name的类型', type(name))
	for name_tule in name:
		print(f'{name_tule},北京欢迎你！{question}')
		
		
# 调用任意数量的参数
welcome_beijing('刘德华', '杨幂', '小码哥', '吴谨言')

# 第二种方法：
print()
list_name = ['刘德华', '杨幂', '小码哥', '吴谨言']
welcome_beijing(*list_name)
welcome_beijing(list_name)
