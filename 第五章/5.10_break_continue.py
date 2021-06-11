# -*- coding: utf-8 -*-
"""
break  -- 终止循环

continue -- 结束本次循环，不在执行CONTINUE后面的语句，然后接着判断
"""
'''
需求：按照学号，从10个人的班级中顺序选5名学生打扫卫生：

1、点到3名的时候，提示还有2个名额
3、点到5名的时候，结束点名

功能点：
1、range(1,11)
2、for
3、continue
4、break
'''

# 动态创建列表
selected_student = []

# 构造10个人
for number in range(1, 11):
	print(f'恭喜您 {number}被选中打扫卫生！')
	selected_student.append(number)
	
	#有一个提醒
	if number == 3:
		print('\t此时，提示还有2个名额')
		
		# 结束本次循环
		continue
		print('我不会被执行！')
		
	if number == 5:
		print('\t结束点名')
		
		# 终止循环
		break

print('恭喜下面的学生被选中打扫卫生：',selected_student)

'''
2、优化猜年龄游戏
'''
print('====================欢迎参加猜年龄游戏====================')

# 实际年龄 25 岁
age = 25

# 计数器控制三次
count_age = 1

#  控制猜测次数
while count_age < 4:
	
	# 用户猜测的年龄
	guess_age = int(input('请输入您猜测的年龄：'))
	
	# 逻辑判断：年龄 3 情况： = 》 《 if -elif -else
	if guess_age == age:
		print('您猜对了，请领取礼物！')
		
		# 终止程序
		break
	elif guess_age > age:
		print('您猜大了！')
		continue
	else:
		print('猜小了！')
	
	count_age += 1

if guess_age != age:
	print('您已经猜测了3次，没有猜对哦')
