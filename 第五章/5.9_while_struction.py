# -*- coding: utf-8 -*-
"""
	while循环
"""
# 计数器
print('请使用 while 构造一个5次的计数器')

count = 0
while count < 5:
	print(f'记录执行了{count}次')
	count += 1
	
print('我已经记录了5次')

'''
猜年龄的游戏

====================欢迎参加猜年龄游戏====================

请输入您猜测的年龄：20

您猜小了！

请输入您猜测的年龄：30

你猜大了哦

请输入您猜测的年龄：28

你猜大了哦

您已经猜了3次，没有机会了哦

# 功能点分析：
1、用户输入 INPUT
2、while
3、 IF

'''
#  实际年龄
age = 25

print('====================欢迎参加猜年龄游戏====================')

# 计数器控制三次
count_age = 1

#  控制猜测次数
while count_age < 4:
	
	# 用户猜测的年龄
	guess_age = int(input('请输入您猜测的年龄：'))
	
	# 逻辑判断：年龄 3 情况： = 》 《 if -elif -else
	if guess_age == age:
		print('您猜对了，请领取礼物！')
	elif guess_age > age:
		print('您猜大了！')
	else:
		print('猜小了！')
	
	count_age += 1
	
print('您没有猜对')




