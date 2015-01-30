# Created by cxy on 15/1/30 with PyCharm
# -*- coding: utf-8 -*-
# 1.2 字符和字符值的转换
# ord()函数得到字符对应的ASCII码或unicode码
lst = map(ord, list("hello, world"))
print lst

# chr()将字符值转为字符
lst2 = map(chr, lst)
print ''.join(lst2)