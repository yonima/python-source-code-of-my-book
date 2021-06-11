# -*- coding: utf-8 -*-
"""
扶摇项目，改了一下代码：
项目实战：《扶摇》之演员简介
（1）构建一个字典，叫Fuyao_Actor_Profile,包括演员名字，饰演角色，配音演员
（2）打印出杨幂扮演的角色是谁？
（3）创建一个备份字典Copy_Fuyao
（4）在演员表中删除阮经天
（5）更替为陈晓
（6）增加新的角色
（7）打印出阮经天所在的演员字典中的演员名及角色名
（8）统计一共有多少角色
（9）重新创建一个新的字典
（10）新字典存放以下信息：
               扶摇的名字、喜欢她的角色有（长孙无极、战北野、小七）、去过的国家（太渊、天权、天煞、璇玑）
"""

# 构建一个字典，叫Fuyao_Actor_Profile,包括演员名字，饰演角色，配音演员
Fuyao_Actor_Profile = {
    '杨幂': {
        'Role_Name': '扶摇',
        'Voice_Actor': '王潇倩'
    },
    '阮经天': {
        'Role_Name': '长孙无极',
        'Voice_Actor': '马正阳'
    },
    '刘奕君': {
        'Role_Name': '齐震',
        'Voice_Actor': '刘奕君'
    },
    '高伟光': {
        'Role_Name': '战北野',
        'Voice_Actor': '赵成晨'
    },
    '高瀚宇': {
        'Role_Name': '江枫',
        'Voice_Actor': '袁聪宇'
    },
    '顾又铭': {
        'Role_Name': '战北恒',
        'Voice_Actor': '林强'
    },
    '王劲松': {
        'Role_Name': '长孙迥',
        'Voice_Actor': '王劲松'
    },
    '黄宥明': {
        'Role_Name': '燕惊尘',
        'Voice_Actor': '文森'
    },
    '秦焰': {
        'Role_Name': '周叔',
        'Voice_Actor': '宣晓鸣'
    },
    '蒋龙': {
        'Role_Name': '小七',
        'Voice_Actor': '苏尚卿'
    }
}
print('目前《扶摇》电视剧的演员列表有：', Fuyao_Actor_Profile)

# （2）打印出杨幂扮演的角色是谁？
print()
#print('杨幂扮演的角色是：', Fuyao_Actor_Profile.get('杨幂').get('Role_Name'))
print('杨幂扮演的角色是：', Fuyao_Actor_Profile['杨幂']['Role_Name'])

# （3）创建一个备份字典Copy_Fuyao
print()
Copy_Fuyao = Fuyao_Actor_Profile.copy()
print('已创建一个备份字典，其内容如下：', Copy_Fuyao)
#test_fuyao = Fuyao_Actor_Profile

# （4）在演员表中删除阮经天
print()
print('---------------')
del Fuyao_Actor_Profile['阮经天']
print(f'删除阮经天的演员列表后:{Fuyao_Actor_Profile}')

# （5）更替为陈晓
Fuyao_Actor_Profile['陈晓'] = {
    'Role_Name': '长孙无极',
    'Voice_Actor': '马正阳'
}
print('修改后的演员字典为：', Fuyao_Actor_Profile)
print()
#print('test 字典',test_fuyao)

# （6）增加新的角色
Fuyao_Actor_Profile['张雅钦'] = {
    'Role_Name': '雅兰珠',
    'Voice_Actor': '吟良犬'
}
Fuyao_Actor_Profile['王鹤润'] = {
    'Role_Name': '凤净梵',
    'Voice_Actor': '蔡娜'
}
Fuyao_Actor_Profile['周俐崴'] = {
    'Role_Name': '时岚',
    'Voice_Actor': '张晗'
}
Fuyao_Actor_Profile['魏晖倪'] = {
    'Role_Name': '简雪',
    'Voice_Actor': '曹一茜'
}
print('------ 6 --------')
print('增加新的角色后，成员名单为：', Fuyao_Actor_Profile)

# （7）打印出阮经天所在的演员字典中的演员名及角色名
# （8）统计一共有多少角色

number_Actor = len(Copy_Fuyao)

# 使用copy后的演员列表，而不是原来的
print('阮经天所在的演员字典中的演员名及角色信息如下:',Copy_Fuyao)


print("阮经天所在的演员字典中一共有", number_Actor, '个角色')

# （9）重新创建一个新的字典
# （10）新字典存放以下信息：
#                扶摇的名字、喜欢她的角色有（长孙无极、战北野、小七）、去过的国家（太渊、天权、天煞、璇玑）
only_fuyao_dict = {
    'Name': '扶摇',
    'Favorited': {'长孙无极', '战北野', '小七'},
    'has_gone_country': {'太渊', '天权', '天煞', '璇玑'}
}
print()
print('扶摇的个人信息字典内容为：', only_fuyao_dict)