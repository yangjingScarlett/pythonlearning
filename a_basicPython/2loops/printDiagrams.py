# coding=utf-8
rows = int(raw_input("please type the row numbers: "))

print "===========等腰直角三角形==========="
for i in range(0, rows):
    for k in range(0, rows - i):
        print "*   ",
        k += 1
    print "\n"
    i += 1

for i in range(0, rows):
    print "* " * (rows - i)
    i += 1

print "===========等边三角形==========="
triangle = []
i = k = 0
for i in range(0, rows):
    line = []
    j = rows - i
    count = 0
    for k in range(0, 2 * rows - 1):
        if k < i:
            line.append(" ")
        else:
            if i % 2 == 0:
                if k % 2 == 0:
                    if count < j:
                        line.append("*")
                        count += 1
                    else:
                        line.append(" ")
                else:
                    line.append(" ")
            else:
                if k % 2 == 0:
                    line.append(" ")
                else:
                    if count < j:
                        line.append("*")
                        count += 1
                    else:
                        line.append(" ")
        k += 1
    triangle.append(line)
    i += 1

for i in triangle:
    for j in i:
        print j,
    print "\n"
