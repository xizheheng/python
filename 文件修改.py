# 将一个文件按行读取，找到要修改的地方，修改后放入新文件中，你用修改的行也放入新文件中。
# 修改yesterday的最后一句“here are so many songs”为“here are no songs”
f = open('yesterday', 'r')
f_new = open('yesterday1', 'w')
for line in f:
    if 'here are so many songs in me that won\'t be sung' in line:
        line = line.replace('here are so many songs', 'here are no songs')
    f_new.write(line)
f.close()
f_new.close()