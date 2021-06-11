# -*- coding: utf-8 -*-
"""
	列表切片操作：
		1、切片概念
		
		2、其他操作操作
			list()函数: 可以用来定义列表，比如把hello，变成列表

			join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

			index方法：返回元素所在的索引位置

			len()函数计算列表的长度

			in 和not in

"""
# 预先定义列表 -- 【扶摇】电视剧人物名
name_fuyao = ['扶摇','周叔','国公','无级太子','医圣','非烟殿主','穹苍']

'''
	1、切片概念
'''
# 指定开始和结束位置，注意不包括最后的位置元素
# 扶摇电视列表中第三个到第五个人物的名字
second_five = name_fuyao[2:5]
print('\n扶摇电视列表中第三个到第五个人物的名字:\n',second_five)

print(type(second_five))

# 不指定开始的位置，则默认从头开始
# 扶摇电视列表中前5个人物名字
z_five = name_fuyao[0:5]
print('\n第一种方法：', z_five)

default_five = name_fuyao[:5]
print('\n第二种方法：', default_five)

# 不指定结束的位置，则从开始位置到结束
# 扶摇电视列表从第6个人物的名字
six_end = name_fuyao[5:]
print('扶摇电视列表从第6个人物的名字',six_end)

# 开始和结束位置都不指定
default_start_end = name_fuyao[:]
print('\n开始和结束位置都不指定:',default_start_end)

# 负数索引表示返回距离列表末位相应距离的元素，也就是取列表中后半部分的元素
# 扶摇电视列表中最后三个人物的名字:
end_three = name_fuyao[-3:]
print('\n扶摇电视列表中最后三个人物的名字:',end_three)

# 取偶数位置的元素
# 扶摇电视列表中偶数位置的人物是:
print('\n扶摇电视列表中偶数位置的人物是:',name_fuyao[::2])

# 取奇数位置的元素
# 扶摇电视列表中奇数位置的人物是
print('\n扶摇电视列表中奇数位置的人物是:',name_fuyao[1::2])

# 逆序列表，相当于reversed(list)
# 另外一个方法逆序
print('\n另外一个方法逆序的方法：',name_fuyao[::-1])

# 在某个位置插入多个元素
# 也可以用同样的方法插入或者删除多个元素

name_fuyao[3:3]=['玄机','太渊','天煞']
print('\n扶摇电视列表中人物变为:',name_fuyao)

# 复制列表,[:] 相当于copy（）,复制以后的新的列表是一个新的，可以对其操作
# new_name_fuyao = name_fuyao 这样的操作是变量赋值，也就是同一个值给了两个变量，一个改变了值 ，另外的两个级跟着修改了。
new_name_fuyao = name_fuyao[:]
print('\n新的列表元素:{}'.format(new_name_fuyao))

new_new = new_name_fuyao
print('new_new:',new_new)
new_name_fuyao.append('璇玑')
print()
print('新的列表被修改',new_name_fuyao)
print('原来的列表被修改',name_fuyao)
print('new_new:',new_new)



'''
	2、其他操作操作
		list()函数: 可以用来定义列表，比如把hello，变成列表

		join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

		index方法：返回元素所在的索引位置

		len()函数计算列表的长度

		in 和not in
		
		三种列表拼接方法
'''
# list()
print()
print('list()函数: 可以用来定义列表:' ,list('hello'))

# join()方法 用于将序列中的元素以指定的字符链接生成一个新的字符串
data_list = ['Python', 'is ', 'No.1']
linked = '-'
print(linked.join(data_list))
print(type(linked.join(data_list)))

# in  or  not in
in_e = '刘德华' in name_fuyao
print('in 的用法:', in_e)

not_in_e = '刘德华' not in name_fuyao
print('in 的用法:', not_in_e)


# 三种列表拼接方法 + / extend() / *
linked_list = name_fuyao + data_list
print('+ linked list :', linked_list)

# 第二种方法
name_fuyao.extend(data_list)
print('\n第二种方法',name_fuyao)

# 第三种拼接
copy_3 = data_list * 3
print('第三种拼接',copy_3)



