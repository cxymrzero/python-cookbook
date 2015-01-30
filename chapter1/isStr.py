# Created by cxy on 15/1/30 with PyCharm
# -*- coding: utf-8 -*-
# 1.3 检测字符串


def is_string(obj):
    return isinstance(obj, basestring)  # basestring是str和unicode对象的父类


def is_exactly_a_string(obj):
    return type(obj) is type('')  # 不要直接比较type


# duck type: 如果它像鸭子, 又能像鸭子叫, 它就是鸭子
# EAFP: Easier to Ask Forgiveness than Permission, 多用try except
def is_string_like(obj):
    try:
        obj + ''
    except:
        return False
    return True


test_str = u'a'
print is_string(test_str)
print is_exactly_a_string(test_str)
print is_string_like(test_str)