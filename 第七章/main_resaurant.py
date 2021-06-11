# -*- coding: utf-8 -*-
import restaurant
import datetime

my_res1 = restaurant.Restaurant('重庆小面', '面馆', 10)
my_res1.get_resInfo()

# 给出固定的时间 9点和23点，测试是否营业
my_res1.get_resWorkingTime(9)
my_res1.get_resWorkingTime(23)
print()

#获取当前时间
now_time = datetime.datetime.now()

print(f"当前时间为{now_time}")
my_res1.get_resWorkingTime(now_time.hour)

print()
my_res1.get_eatingPeople()
my_res1.change_eatingPeople(12)
my_res1.change_eatingPeople(10)

print()
my_res = restaurant.XMRestaurant('小明', '火锅', 10, '四川', 10)
my_res.get_resInfo()
# 正数表示有人入职
my_res.update_employeeNum(1)
# 负数表示离职
my_res.update_employeeNum(-1)
