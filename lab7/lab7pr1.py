'''Jonathan Licht
Lab 7 part 1'''

import time

def F(n):
    if n <= 1:                          #base case
        return n
    else:                               #recursive case
        return F(n-2) + F(n-1)

def f(n):
    num1 = 0
    num2 = 1
    for i in range(n):
        temp = num1
        num1 = num2
        num2 = temp + num1
    return num1


print(f(10))
print(F(10))
'''
t0 = time.time()
F(10)
t1 = time.time()
F(20)
t2 = time.time()
F(30)
t3 = time.time()
F(40)
t4 = time.time()
f(10)
t5 = time.time()
f(20)
t6 = time.time()
f(30)
t7 = time.time()
f(40)
t8 = time.time()

print('F(10) took', t1 - t0, 'seconds')
print('F(20) took', t2 - t1, 'seconds')
print('F(30) took', t3 - t2, 'seconds')
print('F(40) took', t4 - t3, 'seconds')
print('f(10) took', t5 - t4, 'seconds')
print('f(20) took', t6 - t5, 'seconds')
print('f(30) took', t7 - t6, 'seconds')
print('f(40) took', t8 - t7, 'seconds')

'''




