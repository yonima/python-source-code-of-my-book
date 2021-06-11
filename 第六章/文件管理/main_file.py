# -*- coding: utf-8 -*-

"""
     自动化管理文件
     1。 查找
     2。 删除
     3。 重命名
"""
import os
import file_all_op as fo
# 你要查找的文件的绝对路径
path = '/Users/yoni.ma/Pictures/加州'

# 更改工作目录为设置的路径
os.chdir(path)

# os.listdir()方法 ，列出来所有的文件
# 返回path指定的文件夹包含的文件或文件夹的名字的列表。
files = os.listdir(path)

#  显示指令
fo.show_commands()

file_op = int(input('请输入需要执行的操作指令'))

if file_op == 1:
    ''' 查找一个文件 '''
    fo.find_files(files)
elif file_op == 2:
    ''' 删除一个文件'''
    fo.del_files(files)
elif file_op == 3:
    ''' 重命名一个文件 '''
    fo.rename_files(files)
else:
    print('请输入正确的指令: 1 2 或者 3')



