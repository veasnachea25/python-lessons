import os
import random
from math import pi, sin, sqrt, floor, ceil


def arithmetic_operation():
    a = 15
    b = 4
    n1 = a + b # Sum, addition, plus
    n2 = a - b # Difference, substraction, minus
    n3 = a * b # Multiplication, product
    n4 = a / b # Division
    n5 = a % b # Remainder
    n6 = int(a / b) # Quotient ផលចែក
    n7 = a ** b # power, ស្វ័យគុណ, ^ in Matlab
    print('a + b =', n1)
    print('a - b =', n2)
    print('a * b =', n3)
    print('a / b =', n4)
    print('a % b =', n5)
    print('Quotient =', n6)
    print('a ^ b =', n7)
    print('---------------------\n')

    # Increment
    i = 1
    i += 1 # the same as i = i + 1
    print('i =',i)

    j = 2
    j -= 1 # the same as j = j - 1
    print('j =',j)

    k = 2
    k *= 3 # the same as k = k * 3
    print('k =',k)



def mathematic_functions():
    # Default Python function
    print('abs(-2) = ', abs(-2))        # absolute value
    print('3 ^ 2   = ', pow(3,2))       # 3 power 2, បីការេ
    print('Round   = ', round(pi), '\t', round(pi,2)) # បង្គត់លេខ, default python function, not from math library
    print('Min     = ', min(10,20,30))  # minimum
    print('Max     = ', max(10,20,30))  # maximum

    # The functions bellow are taken from 'math' library
    print('Sin(90) = ', sin(pi/2))      # sinus of radian angle
    print('Sqrt(2) = ', sqrt(2))        # squared root
    print('Floor   = ', floor(3.9))     # Find the top integer
    print('Ceil    = ', ceil(3.1))      # Find the bottom integer



def random_number():
    n1 = random.random()      # random number between 0 and 1
    n2 = random.randint(0,10) # random integer between 0 and 10
    print('n1 = ',n1)
    print('n2 = ',n2)



if __name__ == '__main__':
    os.system('clear')
    arithmetic_operation()
    # mathematic_functions()
    # random_number()
