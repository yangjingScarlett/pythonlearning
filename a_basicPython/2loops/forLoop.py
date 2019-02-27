# coding=utf-8

# for loop and else

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            quotient = num / i
            print "%d = %d * %d" % (num, quotient, i)
            break
    # this else will execute when the second for loop's condition is not matching
    else:
        print "%d is a prime number" % num
