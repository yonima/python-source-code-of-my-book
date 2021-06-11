# -*- coding: utf-8 -*-
"""
	for while区别
"""
# 当遍历序列或数组时， 只能用for，while用来遍历会出现死循环
for i in range(10):
	print(i)

'''
# 出现死循环 -- 因为条件一直满足
while i in range(10):
	print(i)

'''
'''
	出现复杂逻辑判断的时候推荐使用 while
需求：
《甄嬛传》之选秀
1。首先创建一个秀女列表，其中魏璎珞不是参选秀女
2。再创建一个空的列表，用来收集已经选中的秀女
整个过程需要修改列表的元素
'''
print('===================')
print('《甄嬛传》之选秀 ')
print('===================')
xiu_nu = ['魏璎珞', '甄嬛','安陵容', '沈眉庄', '夏春']
ru_xuan = []

# 使用while循环选择秀女，直到选择结束
# 把选中的修女收集起来，未选中的删除
while xiu_nu:
	
	kaoshi_xuanyu = xiu_nu.pop()
	print(f"正在参加选秀的修女是：{kaoshi_xuanyu}")
	
	# 判断是否包含魏璎珞
	if kaoshi_xuanyu == '魏璎珞':
		print(f'\t{kaoshi_xuanyu} 不能参加本次选秀,因为她是《延禧攻略》中的人物')
	else:
		print('\t恭喜 {} 入选\n'.format(kaoshi_xuanyu))
		ru_xuan.append(kaoshi_xuanyu)
	
	print(f'还剩下 {xiu_nu} 未参加选秀\n')
	

# 打印所有选中的秀女
print('\n以下是选中的秀女人员名单:')
for index in ru_xuan:
	print('\t'+index)
