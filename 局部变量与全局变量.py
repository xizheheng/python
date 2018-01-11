# 全局变量------->在整个程序中都定义的变量。
# 局部变量------->在某个函数中定义的变量。


# def change_name(name):
#     print('before change:', name)
#     name = 'XIZHEHENG'  # 此处的name为这个函数的局部变量，作用域为这个函数。
#     print('after name:', name)
#
#
# name = 'xizheheng'  # 此处的name为全局变量，作用域为整个程序。
# change_name(name)
# print(name)  # 这个语句执行结果仍然是'xizheheng',所以局部变量的改变，不会影响全局变量。
# #     ---------------python3中不建议局部变量与全局变量使用相同的变量名-----------------------------------


# name = 'xizheheng'  # 字符串全局变量
# name_list = ['xizheheng', 'xiaohei']  # list全局变量
# def change():
#     name = 'xiaohei'  # 在函数中将字符串全局变量进行修改。
#     name_list[0] = 'xijin'  # 在函数中将list全局变量进行修改。
#
#
# print('字符串全局变量修改前', name)
# print('list全局变量修改前', name_list)
# change()
# print('字符串全局变量修改后', name)
# print('list全局变量修改后', name_list)


# 结果： 字符串全局变量修改前 xizheheng
#        list全局变量修改前 ['xizheheng', 'xiaohei']
#        字符串全局变量修改后 xizheheng              字符串全局变量没有改变。
#        list全局变量修改后 ['xijin', 'xiaohei']    list全局变量发生了改变


# 结论：如果全局变量是不可变的。如：字符创，元组，整数。在函数中无法修改。
#      如果是可变的。如列表，元组，字典等。在函数中可以修改。
