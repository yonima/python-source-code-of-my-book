# -*- coding: utf-8 -*-


class Restaurant:
    """ 餐馆类 """
    def __init__(self, resName, resStyle, eatingPeople):
        # 定义属性：餐馆名字和类型，营业时间默认8点，用餐人数
        self.resName = resName
        self.resStyle = resStyle
        self.eatingPeople = eatingPeople
        self.workingTime = '08:00-22:00'

    def get_resInfo(self):
        # 定义方法：第一个打印出餐馆的名字和类型
        print('欢迎在' + self.resName + self.resStyle + '就餐\n', )

    def get_resWorkingTime(self, timeNow):
        # 定义方法：指出餐馆的营业时间，已经正在营业还是休息
        print('本店营业时间为：' + self.workingTime)

        if 8 < timeNow < 22:
            print(f'当前时间是{timeNow}, 餐馆正在营业！')
        else:
            print(f'当前时间是{timeNow}, 餐馆已经休息了！')

    def get_eatingPeople(self):
        # 定义方法：打印出有多少人来用餐
        print('就餐人数为：' + str(self.eatingPeople))

    def change_eatingPeople(self, eatingNum):
        # 定义方法：修改用餐人数，只能递增不能减少
        if eatingNum > self.eatingPeople:
            self.eatingPeople = eatingNum
            print('当前就餐人数修改为：' + str(self.eatingPeople))
        else:
            print(f'由于{eatingNum} < {self.eatingPeople},用餐人数不可以修改，'
                  f' 请输入正确的用餐人数（必须大于）{self.eatingPeople}')


class XMRestaurant(Restaurant):
    """ 定义火锅子类，继承父类 Restaurant """
    def __init__(self, resName, resStyle, eatingPeople, huoguoStyle, employeeNum):
        # 定义自己独有的属性以及父类属性
        super().__init__(resName, resStyle, eatingPeople)
        self.huoguoStyle = huoguoStyle
        self.employeeNum = employeeNum

    def get_resInfo(self):
        # 重写父类的餐馆信息获取方法
        print('欢迎在' + self.resName + self.huoguoStyle + self.resStyle + '就餐\n', )

    def update_employeeNum(self, update_employeeNum):
        # 更新员工人数
        if update_employeeNum < 0:
            # 小于0，表示离职
            self.employeeNum = self.employeeNum + update_employeeNum
            print('离职人数为：' + str(abs(update_employeeNum)) + '人。 员工总人数修改为：' + str(self.employeeNum))

        else:
            # 表示入职
            self.employeeNum = self.employeeNum + update_employeeNum
            print('入职人数为：' + str(abs(update_employeeNum)) + '人。 员工总人数修改为：' + str(self.employeeNum))