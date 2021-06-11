# -*- coding: utf-8 -*-
"""
字典参数：
需求：解决存储未知信息时
目前得知：
  刘德华，年龄30，男性，喜欢去故宫 来自香港，职业是自由职业者，
如果添加：
  收入

"""


def customer(**information):
	print(type(information))
	for key,value in information.items():
		print(f'{key}:{value}')
		
		
# 未知用户的信息时
customer(name='刘德华', age='30', love='故宫',
         place='香港', profession='自由职业者')

'''
第二种方法
'''
dict_customer ={
	 'name': '刘德华',
	 'age': '30',
	 'love': '故宫',
	 'place': '香港',
	 'profession': '自由职业者'
}

print('\n第二种方法')
# 注意必须有**
customer(**dict_customer)

# 区别 函数中的 * 与 **
'''
* 接受任意数量的实际参数，并且转化为元组
** 接受任意数量的关键字实参，并且转化为字典
注意：实际调用时候，*的参数在 **的前面
'''


# 区别
def customer(*name, **information):
	print(type(information))
	print(name)
	for key,value in information.items():
		print(f'{key}:{value}')


list_name = ['小码哥', '杨幂']
# 调用
print('\n 区别')
print('\n第一种调用形式')
customer(list_name, **dict_customer)
print('\n第二种调用形式')
customer(*list_name, **dict_customer)

# 位置错误则出差
# customer(**dict_customer, *list_name)
	
