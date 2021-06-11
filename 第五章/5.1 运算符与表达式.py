# -*- coding: utf-8 -*-
"""
    运算符与表达式
        算术运算符、比较（关系）运算符、赋值运算符、逻辑运算符、位运算运算符、成员运算符以及身份运算符。
"""
my_apple = 7
your_apple = 3

# 算术运算符
print('\n*******************'
      '*'
      '* 算术运算符'
      '*******************\n')
print('加运算符例子：my_apple + your_apple = ',my_apple + your_apple)
print('减运算符例子：my_apple - your_apple = ',my_apple - your_apple)
print('乘运算符例子：my_apple * your_apple = ',my_apple * your_apple)
print('除运算符例子：my_apple / your_apple = ',my_apple / your_apple)
print('取模运算符例子：my_apple % your_apple = ',my_apple % your_apple)
print('取整除运算符例子：my_apple // your_apple = ',my_apple // your_apple)
print('幂运算符例子：my_apple ** your_apple = ',my_apple **your_apple)


# 比较运算符
print('\n*******************'
      '*'
      '* 比较运算符'
      '*******************\n')
print('等于算符例子：my_apple == your_apple = ',my_apple == your_apple)
print('不等于算符例子：my_apple <> your_apple = ',my_apple != your_apple)
print('大于算符例子：my_apple > your_apple = ',my_apple > your_apple)
print('小于运算符例子：my_apple < your_apple = ',my_apple < your_apple)
print('大于等于运算符例子：my_apple >= your_apple = ',my_apple >= your_apple)
print('小于等于运算符例子：my_apple <= your_apple = ',my_apple <= your_apple)


# 位运算符

'''
按位运算符是把数字当作二进制（二进制只有0和1两个数字，十进制就是普通的数字。比如4的二进制就是0100）进行计算的。
Python中的按位运算法则如下：下表中变量 a 为 60，b 为 13二进制格式如下：
a = 0011 1100

b = 0000 1101

-----------------

a&b = 0000 1100

a|b = 0011 1101

a^b = 0011 0001

~a = 1100 0011
'''
print('\n*******************'
      '*'
      '* 位较运算符'
      '*******************\n')
print('\n & 算符例子：my_apple & your_apple = ',my_apple & your_apple)
print('| 算符例子：my_apple | your_apple = ',my_apple | your_apple)
print('^ 算符例子：my_apple ^ your_apple = ',my_apple ^ your_apple)
print('~ 运算符例子：~my_apple  ', ~my_apple)
print('<< 运算符例子：my_apple << 2', my_apple << 2)
print('>> 运算符例子：my_apple >>2  ', my_apple >>2)


# 赋值运算符
print('\n*******************'
      '*'
      '* 赋值运算符'
      '*******************\n')
my_apple += your_apple
print('\n +=  算符例子：my_apple += your_apple; my_apple = ',my_apple)
my_apple -= your_apple
print('-= 算符例子：my_apple -= your_apple; my_apple = ',my_apple)
my_apple *= your_apple
print('*= 运算符例子：my_apple *= your_apple; my_apple = ',my_apple)
my_apple /= your_apple
print('/= 运算符例子：my_apple /= your_apple; my_apple = ',my_apple)
my_apple %= your_apple
print('%= 运算符例子：my_apple %= your_apple; my_apple = ',my_apple)
my_apple //= your_apple
print('//=运算符例子：my_apple //= your_apple; my_apple = ',my_apple)
my_apple **= your_apple
print('**= 算符例子：my_apple **= your_apple; my_apple = ',my_apple)

# 逻辑运算符
print('\n*******************'
      '*'
      '* 逻辑运算符'
      '*******************\n')
print('and 算符例子：my_apple and your_apple; my_apple = ',my_apple and your_apple)
print('or 算符例子：my_apple or your_apple; my_apple = ',my_apple or your_apple)
print('not 算符例子：not my_apple = ',not my_apple)

# 成员运算符
print('\n*******************'
      '*'
      '* 成员运算符'
      '*******************\n')
my_pet = 'dog'
your_pet = 'cat'
animals = ['dog','rabbit','elephant']

if(my_pet in animals ):
    print(f"my pet,{my_pet} ,is in all animals, {animals}")
else:
    print(f'"my pet,{my_pet} ,is not in all animals, {animals}"')

if(your_pet not in animals):
    print(f'your pet ,{your_pet}, is not in all animals, {animals}')
else:
    print(f'your pet ,{your_pet}, is in all animals, {animals}')


'''
    身份运算符
'''

print('\n*******************'
      '*'
      '* 身份运算符'
      '*******************\n')
# 整数的比较

int_data = 30
int_data_2 = 30
print('== 判断变量的值是不是相等：',int_data == int_data_2)
print('is 判断是不是引用同一个对象:',int_data is int_data_2)
print('变量 int_data 的内存地址是:',id(int_data))
print('变量 int_data_2 的内存地址是:',id(int_data_2))
print('\n')

# 字符串的比较
str_data = 'dog'
str_data_2 = 'dog'
print('== 判断变量的值是不是相等：',str_data == str_data_2)
print('is 判断是不是引用同一个对象:',str_data is str_data_2)
print('变量 str_data 的内存地址是:',id(str_data))
print('变量 str_data_2 的内存地址是:',id(str_data_2))
print('\n')

# 列表比较
list_data =[1,2,3]
list_data_2=[1,2,3]
print('== 判断变量的值是不是相等:',list_data == list_data_2)
print('is 判断是不是引用同一个对象:',list_data is list_data_2)
print('变量list_data的内存地址是',id(list_data))
print('变量list_data_2的内存地址是',id(list_data_2))
print('\n')

# 元组比较
tuple_data = ('name','age','location')
tuple_data_2 = ('name','age','location')
print('== 判断变量的值是不是相等:',tuple_data == tuple_data_2)
print('is 判断是不是引用同一个对象:',tuple_data is tuple_data_2)
print('变量tuple_data的内存地址是',id(tuple_data))
print('变量tuple_data_2的内存地址是',id(tuple_data_2))
print('\n')

# 字典比较
dict_data = {"employee id":"0001","employee name":"Nelson",'age':38}
dict_data_2 = {"employee id":"0001","employee name":"Nelson",'age':38}
print('== 判断变量的值是不是相等:',dict_data == dict_data_2)
print('is 判断是不是引用同一个对象:',dict_data is dict_data_2)
print('变量dict_data的内存地址是',id(dict_data))
print('变量dict_data_2的内存地址是',id(dict_data_2))
print('\n')

# 赋值后比较(符合所有数据类型),以LIST为例子介绍：
list_data_3 =[1,2,3]
list_data_4 = list_data_3
print('赋值后比较(符合所有数据类型),以LIST为例子介绍：')
print('== 判断变量的值是不是相等:',list_data_3 == list_data_4)
print('is 判断是不是引用同一个对象:',list_data_3 is list_data_4)
print('变量list_data_3的内存地址是',id(list_data_3))
print('变量list_data_4的内存地址是',id(list_data_4))
print('\n')

# 优先级
number  = 2*2**3 # 幂的优先级大于乘法

print("number is ",number)
number = (2*2)**3 # 使用括号更改优先级顺序
print('使用()优先级以后，number is' , number)

