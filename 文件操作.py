# 文件操作流程
#       1.打开一个文件，得到文件句柄并赋值给一个变量。
#       2.通过句柄对文件进行操作。
#       3关闭文件。

# open()函数就已经打开了一个文件，然后赋给一个变量f，用于对文件的操作。
# open()函数的参数包含<文件名><打开模式>
# <打开模式> "r"-->读模式(默认值)
#           "w"-->写模式(谨慎使用，他的意思是以写的模式创建前面的文件，但是是空的，如果文件之前有内容，则内容会被删除。)
#           "a"-->追加模式(不可以读，只可以在末尾追加。)
#           "r+"-->以读和追加的方式打开，即 r和a  (最多用的)
#           "w+"-->以写和追加的方式打开，即 w和a (没什么卵用)
#           "rb"-->二进制文件读。
#           "wb"-->二进制文件写。

# f = open('yesterday', '<打开模式>')  # 文件句柄，包含了文件在硬盘的相关信息。
# read()函数作用是读取文件的内容，可以理解为一个光标本来在内容的开头，执行函数后光标遍历内容一遍，到了内容的末尾，并停在那。


# 文件的只读
# f = open('yesterday', 'r')
# print(f.read())
# f.write('i love python')  # 当打开模式只有'r'时，文件为只读文件。
# 文件操作完成后要关闭文件
# f.close()


# 读取文件的前几行
# readline()方法每次读取文件内容的一行
# f = open('yesterday', 'r')
# ()方法一次读取文件的一行，然后将光标移动到下一行
#  f.readline()
# 第2个f.readline()读的就是第二行的内容
#  print(f.readline())
# 使用for循环读取接下来的5行内容
#  for i in range(5):
#    print(f.readline())

# 读取文件内容，并且内存中只保存一行.这是------推荐-----的读取文件的方法。
# f变量代表的文件已经变成迭代器。
#    for line in f:
#        print(line)
#    f.close()

# 文件的只写，注：一般不要只写一个'w'，因为他会删除一个已有文件的内容，但是若打开的文件是一个空文件的话，是可以的。
# 'today'文件并不存在，所以它会创建一个文件
#      f = open('today', 'w')
#      f.write('i love python')
#      f.close()


# 文件的追加模式(a),不可以读，但可以在文件末尾添加内容，不做演示。


# tell()返回光标的位置，按字符计数。
# seek()将光标跳到指定位置，按字符计数。
#        f = open('yesterday', 'r')
#        print(f.readline())
#        print(f.tell())
# 将光标跳到文件开头,然后继续读取一行，读取的内容还是第一行
#        f.seek(0)
#        print(f.readline())


# encoding()-->打印文件编码
#        print(f.encoding)


# flush()的用法：刷新缓存，将写的内容时时存储到硬盘中。
#     f = open('today', 'w')
#     f.write('world')
#     f.flush()
#     f.close()


# truncate()-->将指定数字字符后面的内容删掉
#     f = open('today', 'a')
#     f.truncate(2)
#     f.close()


# 实现文件的既能读又能写
#     f = open('today', 'r+')
#     print(f.read())
#     f.write(' ai ni')
#     f.close()


# 注意；Python中向文件中写内容只能在文件的末尾进行追加。不能同如下方式，虽然可以成功，但是会从第5个字符开始对后面的字符进行覆盖，不可取 6。
#    f = open('yesterday', 'r+')
# 让光标跳到第5个字符。
#    f.seek(5)
# 检查是否跳到第5个字符
#    print(f.tell())
# 最后在第5个字符处开始写内容,
#    f.write('1234533333')
#    f.close()


# with代码块执行完毕后，自动关闭文件，对文件的操作在代码块中。
with open('yesterday', 'r') as f:
    pass
