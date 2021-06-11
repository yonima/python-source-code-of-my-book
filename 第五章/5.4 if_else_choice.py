# -*- coding: utf-8 -*-
"""
Python中 4种基本 + 嵌套 选择结构

1、 if

2、 if -- else

3、 if – elif – else

4、 if – elif – elif – xx – else

5、 if – (if – elif – else ) -- else

需求：情人节，西贝推出打折活动：
1、如果您是夫妇：
请接受我们的夫妇套餐，并且享受8折优惠
请帮忙宣传我们的餐馆，多谢！

2、如果您是单身
请接受我们的单身套餐，并且享受9折优惠。
也请帮忙宣传我们的餐馆，多谢！

3、如果您是情侣
请接受我们的情侣套餐，并且享受7.5折优惠。
请帮忙宣传我们的餐馆，多谢！

4、如果您刚分手
请接受我们的安慰套餐，并且享受7折优惠。
也请帮忙宣传我们的餐馆，多谢！

"""
# if语句
merried = True

if merried:
	print('请接受我们的夫妇套餐，并且享受8折优惠!')
	print('也请帮忙宣传我们的餐馆，多谢！')

# if -else 语句
merried = False
print()
if merried:
	print('请接受我们的夫妇套餐，并且享受8折优惠!')
	print('也请帮忙宣传我们的餐馆，多谢！')
else:
	print('请接受我们的单身套餐，并且享受9折优惠。')
	print('也请帮忙宣传我们的餐馆，多谢！')

# if-elif-else 语句
merried = False
double = True # 是否为情侣

print('if-elif-else 语句 演示')
if merried and double:
	print('请接受我们的夫妇套餐，并且享受8折优惠!')
	print('也请帮忙宣传我们的餐馆，多谢！')
elif merried or double:
	print('请接受我们的情侣套餐，并且享受7.5折优惠。')
	print('也请帮忙宣传我们的餐馆，多谢！')
else:
	print('请接受我们的单身套餐，并且享受9折优惠。')
	print('也请帮忙宣传我们的餐馆，多谢！')


# if-elif-elif-else 语句
merried = False
double = False
break_up = True # 判断是否已经分手

print()
print('if-elif-elif-else 语句 演示')

if merried:
	print('请接受我们的夫妇套餐，并且享受8折优惠!')
	print('也请帮忙宣传我们的餐馆，多谢！')
elif double:
	print('请接受我们的情侣套餐，并且享受7.5折优惠。')
	print('也请帮忙宣传我们的餐馆，多谢！')
elif break_up:
	print('请接受我们的安慰套餐，并且享受7折优惠。')
	print('也请帮忙宣传我们的餐馆，多谢！')
else:
	print('请接受我们的单身套餐，并且享受9折优惠。')
	print('也请帮忙宣传我们的餐馆，多谢！')


# 嵌套语句
merried = False
double = False
break_up = True

print()
print('嵌套语句 演示')

#   夫妇 OR  非夫妇 -- 情侣/单身/分手
if not merried:
	if double:
		print('请接受我们的情侣套餐，并且享受7.5折优惠。')
		print('也请帮忙宣传我们的餐馆，多谢！')
	elif break_up:
		print('请接受我们的安慰套餐，并且享受7折优惠。')
		print('也请帮忙宣传我们的餐馆，多谢！')
	else:
		print('请接受我们的单身套餐，并且享受9折优惠。')
		print('也请帮忙宣传我们的餐馆，多谢！')
else:
	print('请接受我们的夫妇套餐，并且享受8折优惠!')
	print('也请帮忙宣传我们的餐馆，多谢！')
	


