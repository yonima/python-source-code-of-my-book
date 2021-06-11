# -*- coding: utf-8 -*-
"""
	类型转化知识点
	1、 type()查看变量类型
	2、 类型直接的互相转化
"""

print('\n各个数值类型的转换')
number = 100

# number的数据类型是 整型，用int表示
print('number的数据类型是：')
print(type(number))

# 将整数转化为浮点数 float()
float_number = float(number)
print('\nfloat_number的数据类型是:')
print(type(float_number))
print(float_number)

# 将整型转化为字符串数 str()
print('\nnumber转化为字符串类型')
str_number = str(number)

print('str_number的数据类型是:')
print(type(str_number))
print(str_number)

# 将字符串转换为整型int()或者浮点数float()
print('\nstr_number转化为数字类型')
int_str_number = int(str_number)

print('int_str_number的数据类型是：')
print(type(int_str_number))
print(int_str_number)

float_str_number= float(str_number)
print('float_str_number的数据类型是:')
print(type(float_str_number))
print(float_number)