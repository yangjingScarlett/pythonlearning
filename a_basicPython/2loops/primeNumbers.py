# coding=utf-8
for num in range(100, 201):
    for i in range(2, num):
        if num % i == 0: break
    else:
        print num
