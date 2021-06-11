class People:
    """定义人 类"""

    def __init__(self, name, location, career):
        self.name = name
        self.location = location
        self.career = career
        self.age = 18  # 默认的属性值，不需要在init方法列表体现

    def introduce_you(self):
        # format()方法的另外一个用法，构造消息。也可以把消息写在一个函数里面，有兴趣的圈友可以试一下
        introduce = ' Python 实战圈的圈友们好，我是{n},今年{a},来自{l}.我的工作是{c},很高兴认识大家！'
        mess = introduce.format(n=self.name,
                                l=self.location,
                                a=self.age,
                                c=self.career)
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


"""
    定义会员类，继承类父类People
    会员类，有自己的属性introduction
"""


class Member (People):
    """会员类，继承人类"""

    def __init__(self, name, location, career, hope):
        super().__init__(name, location, career)
        self.hope = hope

    def introduce_you(self):
        """ 重写父类的方法"""
        introduce = ' Python 实战圈的圈友们好，我是{n},今年{a},来自{l}.我的工作是{c},很高兴认识大家！在咱们圈子里，我希望自己能 {h}.'
        mess = introduce.format(n=self.name,
                                l=self.location,
                                a=self.age,
                                c=self.career,
                                h=self.hope
                                )
        print(mess)

    def set_hope(self, hope):
        """定义子类的方法"""
        self.hope = hope
        print("{}的希望是{}".format(self.name, self.hope))


# 实例化对象
Grace = Member("Grace", "上海", '数据分析师', '彻底学会Python')
# 实现自我介绍
Grace.introduce_you()
# 实现更新年龄
Grace.update_age(19)
# 调用方法更新年龄
Grace.read_age()
# 请修改你的祝福