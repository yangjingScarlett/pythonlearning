# coding=utf-8

import math
import random

# create a object whose type is number
num_var1 = 13
num_var2 = 0

# delete number objects
del num_var1, num_var2

# number has four different types: create int, long integers, float, complex
int_var = -13
long_int_var = 13L
float_var = 13.24
complex_var = 3.14j

print "========== Math Functions =========="
print "abs(%d) = %d" % (int_var, abs(int_var))
print "math.ceil(%f) = %d" % (float_var, math.ceil(float_var))
print "math.cmp(%d, %f) = %d" % (int_var, float_var, cmp(int_var, float_var))
print "exp(1) = %f" % math.exp(1)
print "math.fmod(%f, 2) = %d" % (float_var, math.fmod(float_var, 2))
print "pow(2, 3) = %d" % pow(2, 3)
print "round(%f) = %f" % (float_var, round(float_var))
print "math.sqrt(16) = %f" % math.sqrt(16)
print "\r"

print "========== Random Functions =========="
print "random.choice(range(1,10)) = ", random.choice(range(1, 10))
print "random.random() = ", random.random()
print "random.randrange(0, 100, 2) = ", random.randrange(0, 100, 2)
print "random.uniform(0, 100) = ", random.uniform(0, 100)
print "\r"

print "========== Constants =========="
print "math.e = ", math.e
print "math.pi = ", math.pi
