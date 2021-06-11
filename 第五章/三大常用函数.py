# -*- coding: utf-8 -*-
"""
三大常用函数： enumerate()、zip() 以及 range()
"""
'''
enumerate()

需求： 请输出  XXX 是扶摇电视剧列表中第 XX 角色
      比如：国公 是扶摇电视剧列表中第 2 角色名字
'''
# 定义《扶摇》电视剧人物列表
name_fuyao = ['扶摇','周叔','国公','无级太子','医圣','非烟殿主','穹苍']

# 对列表中每一个元素执行相同的操作
for name in name_fuyao:
    print(name.title()+' 是扶摇电视剧中的角色名字。')

# 如何实现 需求呢？
for index, name in enumerate(name_fuyao):
	print(f'{name} 是扶摇电视剧列表中第 {index} 角色名字')

# 把列表变成字典

# 定义一个空字典
fuyao_dict = {}

for index, name in enumerate(name_fuyao):
	fuyao_dict[index] = name
print('\n把列表变成字典:\n')
print(fuyao_dict)

'''
zip()
需求：请输出 Jack: Python; Andy: Java; Baby: C++
'''
language = ['Python', 'Java', 'C++']
names = ['Jack', 'Andy', 'Baby']

name_zip = zip(names, language)

print('\n需求：请输出 Jack: Python; Andy: Java; Baby: C++')
for name, lang in name_zip:
	print(f'{name}:lang',end='; ')
print(list(name_zip))

'''
range()函数
需求：求10以内对奇数
'''

# 第一种方法:过滤
odd = []
for n in range(10):
    if n % 2 == 1:
        odd.append(n)
print('动态创建列表：需求：求10以内的奇数', odd)

# 第二种方法：range

print('\n第二种方法：range')
for odd in range(1,10, 2):
	print(odd)


# 作业1：请输出[1, 3, 5, 7, 9] ，使用range

# 作业2：求10以内对偶数 (2种方法)

