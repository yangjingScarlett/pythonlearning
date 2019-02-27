# coding=utf-8

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# the items of a list don't need to have same type.
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

# get items of a list
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

# update a list
list3 = ['Baidu', 'Google', 'Bing']
print "Original list3:", list3
list3.append('360')
print "After updating list3:", list3

# delete an item of a list
del list3[len(list3) - 1]
print "After deleting list3:", list3

# operators of list: + * in
list_add = list1 + list2
print "Add two lists into one: ", list_add
list_mul = list3 * 2
print "Multiply two lists into one: ", list_mul
is_in = 3 in list2
print "3 is in %s: %s" % (list2, is_in)

print "========== List Functions =========="
print "list1: ", list1
print "list2: ", list2
print "list1 compare list2: ", cmp(list1, list2)
print "length of list1 :", len(list1)
# [a:b] contains a, not contains b
print "list1[0:len(list1)]", list1[0:len(list1)]
print "max(list2): ", max(list2)
print "min(list2)", min(list2)
