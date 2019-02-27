# coding=utf-8

# identity operators can compare the memory locations of two identifiers
# is: judge if two identifiers are the same object
# is not: judge if two identifier are different objects


a = 20
b = 20
print id(a)  # id() function is for getting the memory location of the object
print id(b)

if a is b:
    print "1 - a 和 b 有相同的标识"
else:
    print "1 - a 和 b 没有相同的标识"

if a is not b:
    print "2 - a 和 b 没有相同的标识"
else:
    print "2 - a 和 b 有相同的标识"

# 修改变量 b 的值
b = 30
if a is b:
    print "3 - a 和 b 有相同的标识"
else:
    print "3 - a 和 b 没有相同的标识"

if a is not b:
    print "4 - a 和 b 没有相同的标识"
else:
    print "4 - a 和 b 有相同的标识"
