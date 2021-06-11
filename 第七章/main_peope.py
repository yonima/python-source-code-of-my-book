"""
    主函数用来调用模块文件中的类
"""
from people import *

print('实例化对象 小马哥')
little_ma = People('小马哥', '北京', '软件工程师')
print('对象调用属性采用逗点表示法.')
print(f'Python 实战圈的圈友们好，我是{little_ma.name},来自{little_ma.location}.我的工作是{little_ma.career},很高兴认识大家！')
print('')
print('对象调用方法，也是采用逗号表示法')
little_ma.introduce_you()

print('\n实例化另外一个对象 kim')
kim = People('Kim', '上海', '数据分析师')
kim.introduce_you()

print()
'''
     两种方法修改属性的值：
     1。通过对象（实例）修改
     2。通过方法设置

'''
# 通过对象修改
little_ma.age = 31
little_ma.read_age()

little_ma.career = '数据分析师'
print('{} 的新职业是{}'.format(little_ma.name, little_ma.career))

# 通过方法修改
little_ma.update_age(33)
little_ma.read_age()
little_ma.update_age(-1)
little_ma.read_age()


"""
    继承的例子
"""
Grace = Member("Grace","上海",'数据分析师','彻底学会Python')
Grace.update_age(19)
Grace.introduce_you()