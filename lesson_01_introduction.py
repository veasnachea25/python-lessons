import os              # import the whole "os" library
import random as rd    # import the library then rename it, alias
from math import sin, pi    # import some properties/function only
from csv import *      # import all children of the library
from pprint import pprint  # advanced print


global_var = 123


def lesson_print():
    print('1. Hello world')
    print('2. Hello','world')
    print('3. Hello','world', sep=';;')
    print('4. Hello world', end='hi\n')
    print('5. Hello world', sep=';;', end='\n')
    print(os.getcwd())
    print(sin(pi/30))
    # pprint(dir(os))



def lesson_variable():
    # data type
    num = 123       # integer
    dec = 123.456   # float, decimal number
    found = True    # boolean: True, False
    name = 'Kosal'  # string with single quote
    phrase = "I'm Tommy." # string with double quote
    desc = """
        very long text
        very long text
    """
    nothing = None  # Empty memory, prefered for declaring object
    print('Data type of num: ', type(num))
    print('Data type of dec: ', type(dec))
    print('Data type of found: ', type(found))
    print('Data type of name: ', type(name))
    print('Data type of nothing: ', type(nothing))

    # Naming convension
    full_name = 'Theang Kosal'  # snake_case, CamelCase
    category_01 = 'A'           # End with number
    C_sharp = 'C#'              # represent C plus plus
    type_ = 'int'               # Avoid the special characters or keyword name

    # Global variable
    print(global_var)



if __name__ == '__main__':
    # lesson_print()
    lesson_variable()
