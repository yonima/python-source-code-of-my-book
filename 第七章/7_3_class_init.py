"""
    类定义知识点：

		1、如何定义一个类
		2、如何定义属性
		3、如何定义方法

"""

class People():
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

