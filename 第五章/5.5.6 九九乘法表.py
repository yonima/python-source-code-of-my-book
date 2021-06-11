# -*- coding: utf-8 -*-
"""
	练习：九九乘法表
"""
for row in range(1, 10):
	for col in range(1,row+1):
		print(f'{row} * {col} = {row * col}', end='  ')
	# 为了控制换行
	print()