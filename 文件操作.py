# 文件操作流程
#       1.打开一个文件，得到文件句柄并赋值给一个变量。
#       2.通过句柄对文件进行操作。
#       3关闭文件。


# 第一种打开文件方法
#         f = open('文件名', 打开模式)
#         f.操作
#         f.close()
# 第二种打开文件的方式
#         with open('文件名', 打开模式)as f:
#             f.操作


# <打开模式> r -->读模式(默认值)
#           w -->写模式(谨慎使用，他的意思是以写的模式创建文件，但是是空的，如果文件之前有内容，则内容会被删除。)
#           a -->追加模式(不可以读，只可以在末尾追加。)
#           r+ -->以读和写的方式打开。在光标处进行覆盖写入(不推荐使用)。
#           rb -->二进制文件读。
#           wb -->二进制文件写。


# 一.文件的操作

# read()函数作用是一次读取文件的所有内容。可以理解为一个光标本来在内容的开头，执行函数后光标遍历内容一遍，到了内容的末尾，并停在那。
# wirte()函数向文件中写入内容。
# tell()返回光标(文件句柄指针)的位置，按字符个数计数。
# seek()将光标(文件句柄指针)跳到指定位置，按字符个数计数。
# readlines()返回一个列表，每一行为一个元素。
# readline()每次读取一行内容。
# enumerate()？？？？
# encoding()打印文件的编码。


# 替换文件的第10行为‘-----’
#         方法1：适合读小文件（low）
#         with open('yesterday', 'r')as f:
#             for index, line in enumerate(f.readlines()):
#                 if index == 9:
#                     print('------')
#                     continue
#                 print(line.strip())


#         方法2（right）
#         count = 0
#         with open('yesterday', 'r')as f:
#             for line in f:
#                 count += 1
#                 if count == 10:
#                     print('-------')
#                     continue
#                 print(line.strip())


# 打印文件的前五行
#         count = 0
#         with open('yesterday', 'r')as f:
#             for i in f:
#                 count += 1
#                 if count == 6:
#                     break
#                 print(i.strip())


# flush()的用法：刷新缓存，将缓存的内容实时存储到硬盘中。
#         with open('yesterday', 'r+')as f:
#             f.write('123456789')
#             f.flush()


# python关于文件的写入。
#   当首先对文件进行了读之后，在对文件进行写操作，写的内容就会追加到文件的末尾。
# with open('yesterday', 'r+')as f:
#     f.read(1)
#     f.write('77777')

#   当没有对文件进行读操作，对文件进行写时，会在光标处对文件进行覆盖写操作。(没什么鸟用)
with open('yesterday', 'r+')as f:
    f.seek(40)
    f.write('liuliuliu')
