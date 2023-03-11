import os
import string


def string_concat():
    first_name = 'Theang'
    last_name = 'Kosal'
    age = 28
    height = 1.65 # meter
    statement_1 = 'My name is ' + first_name + ' ' + last_name + '.'  # general method
    statement_2 = 'I am ' + str(age) + ' years old.' # convert number to string before concat
    statement_3 = 'My height is ' + str(height) + ' meter.' # convert float to string
    print('1. ',statement_1)
    print('2. ',statement_2)
    print('3. ',statement_3)



def string_format_1():
    first_name = 'Theang'
    last_name = 'Kosal'
    age = 28
    height = 1.65 # meter

    statement_1 = 'My name is %s %s.' % (first_name, last_name) # normal string
    statement_2_1 = 'I am %d years old.' % age # integer
    statement_2_2 = 'I am %3d years old.' % age # total 3 characters
    statement_2_3 = 'I am %03d years old.' % age # add 0 before if empty
    statement_3_1 = 'My height is %f meter.' % height  # float
    statement_3_2 = 'My height is %.3f meter.' % height  # float, 3 decimal
    statement_3_3 = 'My height is %5.2f meter.' % height  # 5 = total chars, 2 = num decimal
    statement_3_4 = 'My height is %05.2f meter.' % height  # float, replace 0 before if empty
    print('1.  ',statement_1)
    print()
    print('2.1 ',statement_2_1)
    print('2.2 ',statement_2_2)
    print('2.3 ',statement_2_3)
    print()
    print('3.1 ',statement_3_1)
    print('3.2 ',statement_3_2)
    print('3.3 ',statement_3_3)
    print('3.4 ',statement_3_4)



def string_format_2():
    first_name = 'Theang'
    last_name = 'Kosal'
    age = 28
    height = 1.65 # meter
    statement_1 = 'My name is {0:s} {1:s}.'.format(first_name, last_name) # normal string
    statement_2_1 = 'I am {0:d} years old.'.format(age) # integer
    statement_2_2 = 'I am {0:3d} years old.'.format(age) # total 3 characters
    statement_2_3 = 'I am {0:03d} years old.'.format(age) # add 0 before if empty
    statement_3_1 = 'My height is {0:f} meter.'.format(height)  # float
    statement_3_2 = 'My height is {0:.3f} meter.'.format(height)  # float, 3 decimal
    statement_3_3 = 'My height is {0:5.2f} meter.'.format(height)  # 5 = total chars, 2 = num decimal
    statement_3_4 = 'My height is {0:05.2f} meter.'.format(height)  # float, replace 0 before if empty
    print('1.  ',statement_1)
    print()
    print('2.1 ',statement_2_1)
    print('2.2 ',statement_2_2)
    print('2.3 ',statement_2_3)
    print()
    print('3.1 ',statement_3_1)
    print('3.2 ',statement_3_2)
    print('3.3 ',statement_3_3)
    print('3.4 ',statement_3_4)



def string_format_3():
    first_name = 'Theang'
    last_name = 'Kosal'
    age = 28
    height = 1.65 # meter
    rate = 0.025 # percent
    statement_1 = f'My name is {first_name} {last_name}.'
    statement_2 = f'I am {age} years old.'
    statement_3 = f'My height is {height} meter.'
    statement_4 = f'Interest rate is {rate*100}% per month.'
    print('1. ',statement_1)
    print('2. ',statement_2)
    print('3. ',statement_3)
    print('4. ',statement_4)



def string_format_4():
    # No alignment
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



def string_methods():
    name = 'Theang Kosal'
    print('Original string   : ', name)
    print('- Upper case      : ', name.upper())
    print('- Lower case      : ', name.lower())
    print('- Title case      : ', name.title()) # capitalize each word
    print('- Left 3 letters  : ', name[0:3])
    print('- Right 5 letters : ', name[-5:])
    print('- Mid 4 letters   : ', name[2:6])
    print('- Inject string   : ', name[0:6] + ' Mohamed ' + name[7:])
    print('- Replace string  : ', name.replace('g','Z'))
    print("- Replace once    : ", name.replace('a','X', 1)) # replace letter a one time
    print("- String length   : ", len(name))
    print("- Index of K      : ", name.index('K')) # find index of any character or substring in the string
    print("- Count letter a  : ", name.count('0'))
    print("- Check if exist  : ", 'n' in name)
    print("- Start with 'Th'?: ", name.startswith('Th'))
    print("- End with 'ng'?  : ", name.endswith('ng'))
    print("- Split into list : ", name.split(' '))  # convert string to list (of rnext lesson)
    print("- String Expension: ", 'abc ' * 2)



def string_module():
    print('digits           :', string.digits)
    print('ascii_lowercase  :', string.ascii_lowercase)
    print('ascii_uppercase  :', string.ascii_uppercase)
    print('ascii_letters    :', string.ascii_letters)



def string_unicode():
    first_name = 'ធៀង'
    last_name = 'កុសល'
    print('type', type(first_name))
    print('First Name:', first_name)
    print('Last Name :', last_name)
    print('Full Name :', first_name + ' ' + last_name)
    print('Full Name : %s %s ' % (first_name, last_name))

    print('\u1780\u1781') # កខ



if __name__ == '__main__':
    os.system('clear')
    string_concat()
    # string_format_1()
    # string_format_2()
    # string_format_3()
    # string_format_4()
    # string_methods()
    # string_module()
    # string_unicode()
