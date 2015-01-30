# Created by cxy on 15/1/30 with PyCharm
# -*- coding: utf-8 -*-
# 1.1 字符处理

# 转化为list
lst = list("the string")
print lst

# 循环遍历
for _ in "the string":
    print _

# 列表推导
res1 = [_ for _ in "the string"]
print res1

# map
res2 = map(lambda x: x*2, "the string")
print res2

# 集合操作
# 2.7将set作为默认的数据类型, sets模块失效
set1 = set('abcde')
set2 = set('bcdef')
print ''.join(set1 & set2)