# -*- coding: utf-8 -*-
"""
	字符串知识点：

	1、字符串基本用法：添加空白、链接字符串
	2、字符串的常见运算
		A 修改字符串的大小写
		B 字符串分割
		C 删除两边的空白
		D 其他常见操作
	3、字符串切片
"""

'''
字符串基本用法：

'''
# 转意字符串(\)
print('演示\的用法')
command = 'Let\'s go!'
print('\n使用转移字符输出 ： ', command)

# 添加空白 \n表示换行 \t表示制表符，把文字空两格输出
# 制表符可以组合使用
print('\n\t欢迎大家来到Python实战圈。/n')

# 链接字符串,使用加号  +
print()
log_1_str = 'The error is a bug.'
log_2_str = ' We should fix it.'
print(log_1_str + log_2_str)

'''
	字符串的常见运算
'''
# A: 字符串大小写转换
welcome = 'Hello, welcome to python  practical circle'
# 每个单词的首字母大写， title()
# 函数与方法的区别
print(welcome.title())
# 段落的首字母大写， capitalize()
print(welcome.capitalize())
# lower(), 所有字母小写
print(welcome.lower())
# upper(), 所有字母大写
print(welcome.upper())

# 大写转小写，小写转大写 swapcase()
print(welcome.swapcase())
# String.isalnum() 判断字符串中是否全部为数字或者英文,符合就返回True，不符合就返回False，如果里面包含有符号或者空格之类的特殊字符也会返回False。
print(welcome.isalnum())
# String.isdigit() 判断字符串中是否全部为整数
print(welcome.isdigit())

print()
# B: 字符串分割
string_example = 'Now is better than never .'

# 分割
print('分割字符串： ',string_example.split())
# 安装某一个字母分割
print('按照指定的字母分割字符串: ',string_example.split('n'))
# 去掉换行符，以换行符分割成列表
print('以换行符为分割','1+2\n+3+4'.splitlines())

print()
# C: 删除两边的空白
love_python = '  Hello, Python Practical Circle  '
# 去除字符串两端的空白
print(love_python.strip())
# 去除字符串右侧的空白
print(love_python.rstrip())
# 去除字符串左侧的空白
print(love_python.lstrip())


'''
其他常见操作
'''
print()
print(len(love_python))

'''
	字符串切片
'''
print()
# 字符串切片 与列表切片一样
word = 'python'
print(word[1:2])
print(word[-2:])
print(word[-1])
print(word[::-1])
