# -*- coding: utf-8 -*-
"""
	bool 布尔类型知识点
	0、概念
	1、与或非运算
	2、布尔类型与数值相加
	3、短路运算
"""
'''
	概念 True or False 首字母大小
'''
print(True)
#print(ture)


'''
1.1、与非运算: and
只有两个布尔值都为True时，计算结果才为True
'''
print(True and True)
print(False and True)
print(True and False)
print(False and False)


'''
1.2、或运算: or
只要有一个布尔值True,计算结果为True
'''
print()
print('or 运算演示')
print(True or True)
print(False or True)
print(True or False)
print(False or False)

'''
1.3、非运算: not
True -> False
False -> True
'''
print()
print('not 运算演示')
print(not True)
print(not False)


'''
2、与数值相加:数字 0 表示 False，用 1 表示 True
'''
print()
print(' 相加 运算演示')
print(4 + True)
print(4 + False)

print(4 - True)
print(4 - False)

print(4 * True)
print(4 * False)

print(4 / True)
# print(4 / False)


'''
3、布尔类型与其他数据类型做与或非运算，比如字符串等 ''
规则：
	1、Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True
	2、短路运算
'''
a = True
print(a  and 'a = T' or 'a = F')


