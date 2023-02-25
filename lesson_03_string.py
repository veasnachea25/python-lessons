import os



def string_concat():
    first_name = 'Theang'
    last_name = 'Kosal'
    age = 28
    height = 1.65
    statement_1 = 'My name is ' + first_name + ' ' + last_name + '.' # simple method
    statement_2 = 'I am ' + str(age) + ' years old.'
    statement_3 = 'My height is ' + str(height) + ' meter.'
    print('1. ',statement_1)
    print('2. ',statement_2)
    print('3. ',statement_3)
    print()



def string_format_1():
    first_name = 'Theang'
    last_name = 'Kosal'
    age = 28
    height = 1.65

    # s for string, d for integer, f = float
    statement_1 = 'My name is %s %s.' % (first_name, last_name)
    statement_2_1 = 'I am %d years old.' % age # integer
    statement_2_2 = 'I am %3d years old.' % age # total 3 characters
    statement_2_3 = 'I am %03d years old.' % age # add 0 before if empty
    statement_3_1 = 'My height is %f meter.' % height # float
    statement_3_2 = 'My height is %.2f meter.' % height # 3 decimal
    statement_3_3 = 'My height is %5.2f meter.' % height # 5 = total chars, 2 = num decial
    statement_3_4 = 'My height is %05.2f meter.' % height # add 0 before if empty

    print('1. ',statement_1)
    print()
    print('2.1 ',statement_2_1)
    print('2.2 ',statement_2_2)
    print('2.3 ',statement_2_3)
    print()
    print('3.1 ',statement_3_1)
    print('3.2 ',statement_3_2)
    print('3.3 ',statement_3_3)
    print('3.4 ',statement_3_4)
    print()



def string_format_2():
    first_name = 'Theang'
    last_name = 'Kosal'
    age = 28
    height = 1.65


    statement_1 = 'My name is {0:s} {1:s}.'.format(first_name, last_name)
    statement_2_1 = 'I am {0:d} years old.'.format(age) # integer
    statement_2_2 = 'I am {0:3d} years old.'.format(age) # total 3 characters
    statement_2_3 = 'I am {0:03d} years old.'.format(age) # add 0 before if empty
    statement_3_1 = 'My height is {0:f} meter.'.format(height) # float
    statement_3_2 = 'My height is {0:.2f} meter.'.format(height) # 3 decimal
    statement_3_3 = 'My height is {0:5.2f} meter.'.format(height) # 5 = total chars, 2 = num decial
    statement_3_4 = 'My height is {0:05.2f} meter.'.format(height) # add 0 before if empty

    print('1. ',statement_1)
    print()
    print('2.1 ',statement_2_1)
    print('2.2 ',statement_2_2)
    print('2.3 ',statement_2_3)
    print()
    print('3.1 ',statement_3_1)
    print('3.2 ',statement_3_2)
    print('3.3 ',statement_3_3)
    print('3.4 ',statement_3_4)
    print()



def string_format_3():
    first_name = 'Theang'
    last_name = 'Kosal'
    age = 28
    height = 1.65
    rate = 0.025 # percent

    statement_1 = f'My name is {first_name} {last_name}'
    statement_2 = f'I am {age} years old.'
    statement_3 = f'My height is {height} meter.'
    statement_4 = f'Interest rate is {rate*100}% per month.'

    print('1. ',statement_1)
    print('2. ',statement_2)
    print('3. ',statement_3)
    print('4. ',statement_4)
    print()


def string_format_4():
    # No alignment = left
    print('\n\nNo alignment')
    print('{0} {1}'.format(0, 10**0))
    print('{0} {1}'.format(1, 10**1))
    print('{0} {1}'.format(2, 10**2))
    print('{0} {1}'.format(3, 10**3))
    print('{0} {1}'.format(4, 10**4))
    print('{0} {1}'.format(5, 10**5))
    print('{0} {1}'.format(6, 10**6))
    print('{0} {1}'.format(7, 10**7))
    print('{0} {1}'.format(8, 10**8))
    print('{0} {1}'.format(9, 10**9))

    # Right alignment
    print('\n\nRight alignment')
    print('{0:>3} {1:>16}'.format(0, 10**0))
    print('{0:>3} {1:>16}'.format(1, 10**1))
    print('{0:>3} {1:>16}'.format(2, 10**2))
    print('{0:>3} {1:>16}'.format(3, 10**3))
    print('{0:>3} {1:>16}'.format(4, 10**4))
    print('{0:>3} {1:>16}'.format(5, 10**5))
    print('{0:>3} {1:>16}'.format(6, 10**6))
    print('{0:>3} {1:>16}'.format(7, 10**7))
    print('{0:>3} {1:>16}'.format(8, 10**8))
    print('{0:>3} {1:>16}'.format(9, 10**9))
    print('{0:>3} {1:>16}'.format(10, 10**10))




if __name__ == '__main__':
    os.system('clear')
    # string_concat()
    # string_format_1()
    # string_format_2()
    # string_format_3()
    string_format_4()
