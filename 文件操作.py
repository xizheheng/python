"""文件操作流程
        1.打开一个文件，得到文件句柄并赋值给一个变量。
        2.通过句柄对文件进行操作。
        3关闭文件。
"""
# open()函数就已经打开了一个文件，然后赋给一个变量f，用于对文件的操作。
# open()函数的参数包含<文件名><打开模式>
# <打开模式> "r"-->读模式(默认值)
#           "w"-->写模式(谨慎使用，他的意思是以写的模式创建前面的文件，但是是空的，如果文件之前有内容，则内容会被删除。)
#           "a"-->追加模式(即可以读，也可以写，也就是在末尾追加。
f = open('yesterday')  # 文件句柄，包含了文件在硬盘的相关信息。
# read()函数作用是读取文件的内容，可以理解为一个光标本来在内容的开头，执行函数后光标遍历内容一遍，到了内容的末尾，并停在那。
content = f.read()
