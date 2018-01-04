"""一.集合的用途
    集合是一个无序，不重复的数据类型。
    1.去除重复的元素。
    2.关系测试。例如数学中集合的操作：交集，差集，补集，并集"""
# -------------------------------集合的去除重复功能--------------------------------
# 首先赋值一个list变量
list_1 = [1, 4, 5, 9, 2, 4, 1]
# 使用set()方法，以list类型的变量为参数，这样就将list变量转化为set类型的变量
list_1 = set(list_1)
print(list_1, type(list_1))


# 二.关系测试之交集
# 定义list_2集合类型的变量
list_2 = set([1, 5, 6, 8,])
# 使用intersection()方法，就可以求出俩个集合之间的交集。
print(list_1.intersection(list_2))
# 求交集的运算符 &
print(list_1 & list_2)


# 三.关系测试之并集
# 使用union()方法，求俩个集合的并集
print(list_1.union(list_2))
# 并集的运算符 |
print(list_1 | list_2)


# 四.关系测试之差集。若求list_1和list_2的差集，就是求list_1有，list_2没有的,使用difference()方法。
print(list_1.difference(list_2))
# 求差集的运算符 -
print(list_1 - list_2)
print(list_2.difference(list_1))


# 五.关系测试之子集。
print(list_1.issubset(list_2))
print(list_1.issuperset(list_2))

# 六.对称差集。即除去俩个集合之间相同的部分组成一个集合。
print(list_1.symmetric_difference(list_2))
# 对称差集的符号 ^
print(list_1 ^ list_2)
print("----------------")


# isdisjoint()方法的功能是如果他们之间没有交集，返回True。
print(list_1.isdisjoint(list_2))


# 集合添加一项元素，使用add()方法
list_1.add(100)
print(list_1)

# 集合添加多项，使用update()方法,其参数为一个列表
list_1.update([1000, 45, 789])
print(list_1)


# 集合删除元素，使用remove()方法
list_1.remove(1)
print(list_1)


# 判断元素是否在集合中
# x in set

