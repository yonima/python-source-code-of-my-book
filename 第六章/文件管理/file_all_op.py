# -*- coding: utf-8 -*-
import os

def show_commands():
    """
        提示用户输入的操作
    :return:
    """
    print('-----------------------')
    print(' 请用户输入不同的指令')
    print('1 模糊查找文件')
    print('2 删除一个文件')
    print('3 重命名一个文件')
    print('-----------------------')


def find_files(files):
    """
        模糊查找文件
    :param files: files
    :return:
    """
    find_file = input('请输入需要模块查找的文件名字')
    end_file = input('请输入文件的类型')
    for f in files:
        ''''
            对于关键字的查找，使用IF判断语句
            in的用法：判断某一个成员是不是在某一个字符串里面
            f.endswith()方法用来判断文件结尾
        '''
        if find_file in f and f.endswith(end_file):
            print(f'找到文件名中包括 {find_file},并且文件类型是 {end_file} 的完整文件名字有：{f}')


def del_files(files):
    """
    删除指定的文件
    :param files:
    :return:
    """
    del_file = input('请输入需要删除的文件名')
    if del_file in files:
        ''' 首先判断文件是否存在'''
        print(f'您将删除 {del_file}')

        # 确认是否删除
        confirm = input('请再次确认是否删除(Y/N)')

        if confirm == 'Y':
            os.remove(del_file)
            print(f'您已经删除{del_file}')
    else:
        print(f'文件 {del_file}不存在, 无法删除')


def rename_files(files):
    """
    重命名指定的文件
    :param files:
    :return:
    """
    rename_file = input('请输入需要重命名的文件名')
    newname_file = input('请输入新的文件名')

    if rename_file in files:
        print(f'文件{rename_file}存在，将被重命名为{newname_file}')
        os.rename(rename_file, newname_file)

    else:
        print(f'文件{rename_file} 不存在，无法重命名')
