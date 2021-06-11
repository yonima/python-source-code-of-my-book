# -*- coding: utf-8 -*-
"""
	字典 + 列表 知识点

	1、字典列表
	
	2、在字典中存储列表

	3、在字典中存储字典

"""
'''
1、字典列表
'''
name_dict = {'name':'Python','Age':18}
name_2_dict = {'name':'Jave','Age':'unknown'}

name_list = [name_dict, name_2_dict]
print(name_list)
print(type(name_list))


'''
2、在字典中存储列表
’客户1‘:[’姓名‘,’职业',’年龄'],
 ’客户2':['魏璎珞','富察皇后','纯妃','高贵妃'],
‘客户3':'皇上'
'''
cust_dict = {
	'客户1':['姓名','职业','年龄'],
	'客户2':['魏璎珞','富察皇后','纯妃','高贵妃'],
	'客户3':'皇上'
}

print()
print(cust_dict)
print(type(cust_dict))

'''
3、在字典中存储字典
 '爱上不该爱的人' {
            '姓名':'魏璎珞',
            '职位':"妃子",
            '年薪':'300两',},
 
    '只爱皇上'{
            '姓名':'高贵妃',
            '职位':'贵妃',
            '年薪':'800两',}

'''


net_name_dict_dict= {
	'爱上不该爱的人':{
            '姓名':'魏璎珞',
            '职位':"妃子",
            '年薪':'300两'},
	
	'只爱皇上':{
			'姓名':'高贵妃',
            '职位':'贵妃',
            '年薪':'800两'}
}
print()
print(net_name_dict_dict)
print(type(net_name_dict_dict))
