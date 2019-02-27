# coding=utf-8
a = 21
b = 10
c = 0

if a == b:
    print a, " == ", b
else:
    print a, " not == ", b

if a != b:
    print a, " != ", b
else:
    print a, " == ", b

if a < b:
    print a, " < ", b
else:
    print a, " not < ", b

if a > b:
    print a, " > ", b
else:
    print a, " not > ", b

# 修改变量 a 和 b 的值
a = 5
b = 20
if a <= b:
    print a, " <= ", b
else:
    print a, " not <= ", b

if b >= a:
    print b, " >= ", a
else:
    print b, " not >= ", a
