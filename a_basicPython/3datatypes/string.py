# coding=utf-8
import sys

reload(sys)
print sys.getdefaultencoding()
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

str_var1 = "Hello Python!"
str_var2 = "Hello World!"

# del str_var1
# del str_var2

print "========== Get Substring of a String =========="
print "str_var1 = %s, str_var1[0] = %s" % (str_var1, str_var1[0])
print "str_var2 = %s, str_var2[1:5] = %s" % (str_var2, str_var2[1:5])
print "\r"

print "========== Update a String =========="
print "get a new string: ", str_var1[0:5] + " This is Python!"
print "\r"

print "========== Escape Characters =========="
print r"\ : " \
      "continuation character"
print r"\\ : backslash"
print r"\' : single quotation mark"
print r"\" : double quotation marks"
print r"\a : bell"
print r"\b : backspace"
print r"\000 : blank"
print r"\n : new line"
print r"\r : enter"
print r"\v : vertical tab"
print r"\t : horizontal tab"
print "\r"

print "========== String Functions =========="
count = 1
print "%d.把字符串的第一个字符大写：\r\n str.capitalize('hello') = %s" % \
      (count, str.capitalize("hello"))
count += 1

print "%d.原字符串居中，并用给定字符填充至指定长度：\r\n str.center('hello', 15, '*') = %s" % \
      (count, str.center("hello", 15, "*"))
count += 1

print "%d.原字符串居左，并用给定字符填充至指定长度：\r\n str.ljust('hello', 15, '*') = %s" % \
      (count, str.ljust("hello", 15, "*"))
count += 1

print "%d.原字符串居右，并用给定字符填充至指定长度：\r\n str.rjust('hello', 15, '*') = %s" % \
      (count, str.rjust("hello", 15, "*"))
count += 1

print "%d.计算 'l' 在 'hello' 里面出现的次数：\r\n str.count('hello', 'l') = %s" % \
      (count, str.count('hello', 'l'))
count += 1

print "%d.以指定的编码格式解码：\r\n str.decode('你好', encoding='utf-8') = %s" % \
      (count, str.decode('你好', encoding='utf8'))
count += 1

print "%d.以指定的编码格式编码：\r\n str.encode('你好', encoding='utf-8') = %s" % \
      (count, str.encode('你好', encoding='utf-8'))
count += 1

print "%d.检查字符串是否以给定的字符结束：\r\n str.endswith('hello','o') = %s" % \
      (count, str.endswith('hello', 'o'))
count += 1

print "%d.检查字符串是否以给定的字符开始：\r\n str.startswith('hello', 'h') = %s" % \
      (count, str.startswith('hello', 'h'))
count += 1

print "%d.将 tab 符号转为空格，tab 符号的默认空格数为8个：\r\n str.expandtabs('h\te\tl\tl\to') = %s" % \
      (count, str.expandtabs('h\te\tl\tl\to'))
count += 1

print "%d.查找 string 中是否有某个 substring, 如果有返回开始的索引值，否则返回-1：\r\n " \
      "str.find('hello, this is python', 'o') = %s" % \
      (count, str.find('hello, this is python', 'o'))
count += 1

print "%d.获取 substring 在 string 中的索引，类似find(): \r\n str.index('Hello', 'l') = %s" % \
      (count, str.index('Hello', 'l'))
count += 1

print "%d.格式化字符串：Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。\n" \
      "基本语法是通过 {} 和 : 来代替以前的 百分号 。\r\n str.format('{0}, this is {1}', 'hello', 'python') = %s" % \
      (count, str.format('{0}, this is {1}', 'hello', 'python'))
count += 1

print "%d.判断 string 是否只含有字母或数字：\r\n str.isalnum('hello1234') = %s" % \
      (count, str.isalnum('hello1234'))
count += 1

print "%d.判断 string 是否只含有字母（不包括空格和符号）：\r\n str.isalpha('hello!') = %s" % \
      (count, str.isalpha('hello!'))
count += 1

print "%d.判断 string 是否只含有数字：\r\n str.isdigit('1234507896') = %s" % \
      (count, str.isdigit('1234507896'))
count += 1

print "%d.判断 string 中的字母是否都是小写字母（没有字母返回false）：\r\n str.islower('hello1234') = %s" % \
      (count, str.islower('hello1234'))
count += 1

print "%d.判断 string 中的字母是否都是大写字母（没有字母返回false）：\r\n str.isupper('1234567890') = %s" % \
      (count, str.isupper('1234567890'))
count += 1

print "%d.将 string 中的小写字母转换为大写字母：\r\n str.upper('hello1234') = %s" % \
      (count, str.upper('hello1234'))
count += 1

print "%d.将 string 中的大写字母转换为小写字母：\r\n str.lower('HellO1234') = %s" % \
      (count, str.lower('HellO1234'))
count += 1

print "%d.判断 string 中是否只有空格：\r\n str.isspace('    ') = %s" % \
      (count, str.isspace('    '))
count += 1

seq = ('hello', 'this', 'is', 'python')
print "%d.合并seq中的字符串为一个新的字符串：\r\n str.join('-', %s) = %s" % \
      (count, seq, str.join('-', seq))
count += 1

print "%d.裁掉字符串左边的空格和换行符和回车符：\r\n str.lstrip('  \r\nhello  ') = %s" % \
      (count, str.lstrip('  \r\nhello  '))
count += 1

print "%d.裁掉字符串右边的空格和换行符和回车符：\r\n str.rstrip('  hello\r\n  ') = %s" % \
      (count, str.rstrip('  hello\r\n  '))
count += 1

print "%d.裁掉字符串左右两边的空格和换行符和回车符(中间的不会被裁掉)：\r\n str.strip('  \r\nhel  lo\r\n  ') = %s" % \
      (count, str.strip('  \r\nhel  lo\r\n  '))
count += 1

print "%d.获取 string 中的最大值：\r\n max('hello') = %s" % \
      (count, max('hello'))
count += 1

print "%d.获取 string 中的最小值：\r\n min('hello') = %s" % \
      (count, min('hello'))
count += 1

print "%d.以 sep 为分割符，将 string 分割为一个三元元组：\r\n " \
      "str.partition('hello this is python what can I do?', 'python') = %s" % \
      (count, str.partition('hello this is python what can I do?', 'python'))
count += 1

print "%d.在 string 中将 str1 替换为 str2：\r\n str.replace('hello, this is python', 'python', 'world') = %s" % \
      (count, str.replace('hello, this is python', 'python', 'world'))
count += 1

print "%d.以 sep 为分隔符, 将 string 分割为一个列表：\r\n " \
      "str.split('hello, this is python, what can I do?', ',') = %s" % \
      (count, str.split('hello, this is python, what can I do?', ','))
count += 1

print "%d.按照行('\\r', '\\r\\n', \\n')分隔，返回一个包含各行作为元素的列表：\r\n " \
      "str.splitlines('hello\\r this is python\\n what can I do?\\r\\n') = %s" % \
      (count, str.splitlines('hello\r this is python\n what can I do?\r\n'))
count += 1


