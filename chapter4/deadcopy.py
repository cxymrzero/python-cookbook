# Created by cxy on 15/1/30 with PyCharm
# -*- coding: utf-8 -*-
# 4.1 How to copy
# 赋值使用的是引用; copy拷贝了每个对象的引用; deepcopy是深拷贝, 递归地拷贝了每个对象
import copy
l = [[1, 2], 3]
l1 = copy.copy(l)
l2 = copy.deepcopy(l)
l3 = list(l)  # 浅拷贝, 比下面两种好
l4 = [i for i in l]  # 不推荐
l5 = l[:]  # 不推荐
l.append(4)
l[0].append(3)
print l1, l2, l3, l4, l5

# 浅拷贝list, dict, set类型可以用对应的函数
d = {'a': [1]}
d0 = copy.deepcopy(d)
d1 = dict(d)
d2 = {}  # 没dict()好(不够简单
for key in d:
    d2[key] = d[key]
d['a'].append(2)
print d, d0, d1, d2

# is判断是否相同, ==判断值是否相等, copy无论浅深都不相同
print l is l1