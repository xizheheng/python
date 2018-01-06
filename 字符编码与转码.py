# utf-8下英文为1字节，中文字符为3字节。Unicode可以可以转化为所有编码。
# 各类编码间的转化，必须decode(解码)为Unicode（utf-8），再encode为其他编码。
# 所有的decode都是解码成Unicode，decode后的参数为当前编码，意思是将当前编码解码为Unicode。
# python3默认编码为Unicode。
# encode将字符集转化为bytes类型
s = '你好'
s_to_gbk = s.encode('gbk')
print(s_to_gbk)