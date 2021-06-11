# -*- coding: utf-8 -*-
"""
字典知识点

    1、定义
        字典名 = { 关键字1：值，关键字2：值，关键字3：值}
        
    2、访问字典

	3、修改键值对

	4、添加键值对

	5、删除键值对（4个方法）

	6、创建空字典
	
	7、内置函数与方法

"""
'''
	定义一个字典：{'',''}
'''
# 构建一个字典，记录各宫嫔妃的年薪银子，单位是两
# '魏璎珞':300,'皇后':1000,'皇贵妃':800,'贵妃':600,'斌':200}
name_dict = {'魏璎珞':300,'皇后':1000,'皇贵妃':800,'贵妃':600,'斌':200}
print('记录各宫嫔妃的年薪银子', name_dict)
print(type(name_dict))

# 字典的两个特性
# key不能出现两次,前面的值会被覆盖
lang_name = {'Name':'Python','Age':13,'Name':'Java' }
print()
print(lang_name)

# key 不能是可变的 -- 列表
# name_dict = {['魏璎珞']:300,'皇后':1000,'皇贵妃':800,'贵妃':600,'斌':200}
# print(name_dict)

'''
    2、访问字典
'''
print('\n皇后的年薪是：', name_dict['皇后'])


'''
	3、修改键值对
'''
name_dict['皇后'] = 900
print('\n修改后的皇后的年薪是：', name_dict['皇后'])
print(name_dict)

'''
	4、添加键值对
'''
name_dict['常在'] = 70
print('\n常在的年薪是:',name_dict['常在'])
print('字典被修改为：',name_dict)

'''
    5、删除键值对（4个方法）
'''
# 第一种方法:del
del name_dict['常在']
print('del删除字典中的常在：',name_dict)


# 第二种方法：pop('key')
print()
weiyingluo = name_dict.pop('魏璎珞')
print('我删除的是是：',weiyingluo)
print('pop 删除字典后：',name_dict)


# 第三种方法 popitem()
print()
pop_end = name_dict.popitem()
print(pop_end)
print('popitem 删除字典后：',name_dict)


# 第四种方法: clear()
name_dict.clear()
print('clear 删除数据后的字典是：',name_dict)

# del name_dict
# print(name_dict)


'''
	6、创建空字典:动态添加
'''
# 定义电影字典
moive = {}
moive['片名']='比悲伤更悲伤的事'
moive['主演']='陈意涵'
moive['排名']=1

print(moive)

'''
	7、内置函数与方法
'''
# 内置函数
# len
print(len(name_dict))
print(len(moive))
print(str(moive))

# 内置方法
print('\n查看moive字典种的key', moive.keys())
print('\n查看moive字典种的value',moive.values())
print('\n查看movie键值对',moive.items())