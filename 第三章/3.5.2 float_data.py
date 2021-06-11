"""
     浮点数运算知识点
     1、四则运算
     2、python3.6 中新的 format方法
     3、浮点数取整数的方法
"""
'''
    第一个四则运算
'''
# 加法
add = 0.2 + 0.1
print(add)
print('求 0.2 + 0.1 = {}'.format(add))

# 减法
print()
sub = 10.9 - 8.1
print(f'10.9 - 8.1 = {sub}')
# 乘法
multi = 0.1 * 3
print(f'0.1 * 3 = {multi}')

# 除
div = 10.0 / 2.0
print(f'10.0 / 2.0 = {div}')

# 取模运算：返回除法的余数
delivery = 7 % 4.3
print(f'7 % 4.3 = {delivery}')

# 取整除，返回商的整数
round_number = 7 // 4.3
print(f'7 // 4.3 = {round_number}')

# 幂运算

power = 7 ** 2.0
print(f'7 ** 2.0= {power}')
'''
    第二个： format()方法是格式化输出，也就是在{}的地方替换为变量的值
    后面几天的内容中，它会被经常被用到
'''

# 3.6 中的format方法
print()
print(f'求 0.2 + 0.1 = {add}')
# 加法的三种输出方法
print()
add = 0.2 + 0.1
print(add)
print('求 0.2 + 0.1 = {}'.format(add))


'''
    第三个：浮点数取整数的方法
    1、向下取整
    2、四舍五入
    3、向上取整
'''
# 1、向下取整 int()函数
salary = 1453.68
int_salary = int(salary)
print(f'向下取整 salary 是 {int_salary}')

# 2、四舍五入 round()函数。第二个参数是保留小数点后多少位，默认是0
salary_round = round(salary, 1)
print(f'salary 四舍五入后是{salary_round}')
round_salary = round(salary)
print(f'salary 四舍五入后是{round_salary}')

# 3、向上取整 math.ceil(第六天)
import math

salary = 1453.68
salary_nelson = 1450.02
ceil_salary = math.ceil(salary)
print(f'向上取整 salary 是{ceil_salary} ')

nelson_ceil = math.ceil(salary_nelson)
print(f'向上取整 salary 是{nelson_ceil}')