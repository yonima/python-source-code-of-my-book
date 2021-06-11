"""
    类定义知识点：
1、如何定义一个类
2、如何定义属性
3、如何定义方法
"""


class People:
    """定义人 类"""
    def __init__(self,name,location,career):
        self.name = name
        self.location = location
        self.career = career
        self.age = 18 # 默认的属性值，不需要在init方法列表体现

    def introduce_you(self):
        # format()方法的另外一个用法，构造消息。也可以把消息写在一个函数里面，有兴趣的圈友可以试一下
        introduce = ' Python 实战圈的圈友们好，我是{n},今年{a},来自{l}.我的工作是{c},很高兴认识大家！'
        mess = introduce.format(n=self.name,
                                l = self.location,
                                a = self.age,
                                c = self.career)
        print(mess)

    def read_age(self):
        # 读取年龄属性
        print('{}今年{}岁'.format(self.name, self.age))

    def update_age(self, new_age):
        # 更新属性的方法
        if new_age < 0:
            print('年龄不能为负数')
        else:
            self.age = new_age

'''
    知识点：如何实例化
什么是实例化
如何创建对象
如何调用对象
'''

print('实例化对象 小马哥')
little_ma = People('小马哥', '北京', '软件工程师')


print('对象调用属性采用逗点表示法.')
print(f'Python 实战圈的圈友们好，我是{little_ma.name},来自{little_ma.location}.我的工作是{little_ma.career},很高兴认识大家！')
print('')
print('对象调用方法，也是采用逗号表示法')
little_ma.introduce_you()

'''
     两种方法修改属性的值：
     1。通过对象（实例）修改
     2。通过方法设置

'''
# 通过对象修改
little_ma.age = 31
print('通过对象修改属性')
little_ma.read_age()

little_ma.career = '数据分析师'
print()
print('{} 的新职业是{}'.format(little_ma.name, little_ma.career))

# 通过方法修改
print()
print('通过方法修改属性')
little_ma.update_age(33)
little_ma.read_age()
little_ma.update_age(-1)
little_ma.read_age()

