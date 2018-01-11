def search(word, file='haproxy'):
    f = open(file, 'r', encoding='utf-8')
    data = f.readline()
    while data:
        if word not in data or 'backend' not in data:  # 要搜索的word和'backend'有一个不在行中
            data = f.readline()
        else:  # 要搜索的word和'backend'都在行中
            # data = f.readline()
            while data and 'global' not in data and 'default' not in data and 'listen' not in data and 'frontend' not in data:
                print(data)
                data = f.readline()
    f.close()
    return True


def add(dic, file='haproxy'):
    pass


arg = {'backend':'www.oldboy.org', 'record': {'server': '100.1.7.9', 'weight': 20,'maxconn': 30}}
arg = eval("arg")
print(arg)
