import sys
import time


"""使用sys库中的stdout(标准输出，即屏幕).write将'#'写到屏幕上
    然后使用stdout的flush刷新缓存，直接输出。
    time.sleep是设置暂停时间。
"""
for i in range(50):
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.5)