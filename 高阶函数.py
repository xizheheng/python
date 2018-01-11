# 高阶函数是指函数的参数可以为函数的函数。
def add(x, y, f):
    """
    高阶函数的演示
    :param x: 普通参数
    :param y: 普通参数
    :param f: 函数参数
    :return: x和y绝对值之和。
    """
    return f(x) + f(y)


result = add(3, -6, abs)
print(result)