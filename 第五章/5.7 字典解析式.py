# -*- coding: utf-8 -*-
"""
	字典解析式：
	1、指定条件的字典解析式
	2、无条件字典解析式
"""
'''
1、指定条件的字典解析式
需求：我们把某培训机构的一部分课程信息存储在字典中，字典中的键为课程名字；值为课程评分。
请筛选出课程评分小于12的课程，我们首先使用 for 循环实现
'''
count_information = {
    'Abbyzhang':1,
    'Abligail':12,
    'Acy':11,
    'Adaa':2,
    'Adalyn':24,
    'Adelaide':13,
    'Afum':10
}
print(f'课程信息{count_information}')

# 选择小于12分的课程
filter_dict = {}
for key, value in count_information.items():
    if value < 12:
        filter_dict[key] = value
        
print(f'\n选择小于12分的课程有：{filter_dict}')

# 使用字典解析式
filter_dict = {key:value for key, value in count_information.items() if value < 12 }
print(f'\n使用字典解析式找出小于12分的课程：{filter_dict}')

# 为了可读性，断行输出
filter_dict = {
    key:value
    for key, value in count_information.items()
    if value < 12
}

'''
2、无条件列表解析式
需求：互换嫔妃年薪字典的键和值，把年薪作为值
'''
print()
name_dictionary = {'魏璎珞':300,'皇后':1000,'皇贵妃':800,'贵妃':600,'嫔':200}

print('嫔妃年薪字典:',name_dictionary)

# 互换嫔妃年薪字典的键和值，把年薪作为值
new_name_dic = {}
for key, value in name_dictionary.items():
    new_name_dic[value] = key
print('颠倒嫔妃年薪字典的键和值后：',new_name_dic)

# 使用字典解析式

new_name_dic = {value:key for key, value in name_dictionary.items()}
print('使用字典解析式颠倒嫔妃年薪字典的键和值后：',new_name_dic)
# 使用断行显示字典解式

new_new_name_dic = {
    value:key
    for key, value in name_dictionary.items()
}
print('使用断行显示字典解析式颠倒嫔妃年薪字典的键和值后：',new_new_name_dic)
