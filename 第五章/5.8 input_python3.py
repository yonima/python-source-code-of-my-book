# -*- coding: utf-8 -*-
"""
python 用户交互:input()
需求：
	请模拟微博登陆程序
	1、用户名
	2、密码
"""
# 微博系统记录我的账号信息如下
username = 'Tfboy'
password = '123456'

user = input('请您输入您的账号：')
passw = input('请输入您的密码：')

if user == username and passw == password:
	print('欢迎回来，请开始您的微博之旅！')
else:
	print('请输入正确的账号和密码！')


