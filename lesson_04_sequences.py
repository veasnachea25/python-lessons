import os
from pprint import pprint


def lesson_range():
    """
    r = range(start, stop, step)
    """
    r1 = range(0,10)  # = range(0,10,1)
    r2 = range(10,0,-1) # -1 must add for reverse range
    print('type: ', type(r1))
    print(r2)
    print(r2[0])
    print(r2[1])


def lesson_list():
    num_list = [58, 35, 64, 10, 42, 87, 55, 92, 12, 41, 58]
    str_list = ['Kosal','Veasna','Vichet']
    bool_list = [True,False,True,False]
    mix_list = [1, 3.14, 'Kosal', True] # not recommanded
    print('num_list =',num_list)
    print('str_lis  =',str_list)
    print('bool_lis =',bool_list)
    print('mix_lis  =',mix_list)

    ## Get element/value of list
    item_1 = num_list[0] # get the first element in the list, index start from 0
    item_2 = num_list[1] # second element
    item_3 = num_list[-1] # last element
    lst_1 = num_list[1:4] # get slice
    lst_2 = num_list[:3] # get slice fron index 0 to 2
    lst_3 = num_list[1:4] # get slice from index 1 to 3
    lst_4 = num_list[4:1:-1] # reverse order
    print(lst_4)

    ## Add more element
    num_list.append(123) # add new element to last
    num_list.extend([100, 200]) # append list to the list
    print('new list =',num_list)

    ## Edit value
    num_list[2] = 64000000
    print('new list',num_list)

    ## Reverse the list
    num_list.reverse()  # first method (preferable)
    lst_5 = reversed(num_list)  # second method
    lst_6 = num_list[::-1]      # third method

    ## Sort list
    num_list.sort(reverse=True) # First method
    lst_7 = sorted(num_list)
    print('new list =',num_list)
    print('new list =',lst_7)

    ## Delete/Remove element
    del num_list[0]   # delete by index of value
    del num_list[0:3] # delete by index of slice
    num_list.remove(42) # remove the value, not the index
    dv = num_list.pop(0) # delete by index, then paste the value to a variable
    print(f'the value {dv} has been deleted')
    print('deleted value =',dv)
    num_list.clear()  # remove all elements, become empty list
    print('new list =',num_list)

    ## List methods
    # pprint(dir(num_list))
    length = len(num_list)  # find the length or size of the list
    total = sum(num_list)  # sum the list of number
    idx = num_list.index(92) # find the index of the value
    cnt = num_list.count(58) # count frequency of the value in the list
    print('length =',length)
    print('total =',total)
    print('index =',idx)
    print('count 58 =',cnt)



def lesson_tuple():
    T = (1, 3, 5, 7, 9)
    genders = ('Male','Female')
    L = list(T)  # convert tuple to list
    print(T.count())
    print(T.index(3))
    print(T, type(T))
    print(L, type(L))



def lesson_set():
    # https://www.programiz.com/python-programming/methods/set/remove

    # Sets
    A = {1, 3, 5, 7, 9}
    B = {2, 3, 5, 7, 11}
    C = {2, 3, 8, 9, 10}
    D = {1, 3}

    ## Mathematics of set
    A_only = A.difference(B)  # returns items present only in set A, equivalent to A-B
    B_only = B.difference(A)  # returns items present only in set B, equivalent to B-A
    I = A.intersection(B,C)   # Intersect set between A and B
    U = A.union(B,C)          # Union set between A and B
    found_1 = D.issubset(A)   # all items of D are present in A
    found_2 = A.issuperset(D) # A is parent of D, opposite of issubset

    """
    s.add()
    s.clear()
    s.pop()
    s.isdisjoint()
    s.setdiscard()
    s.copy()
    """



def lesson_dictionary():
    # Dictionary = json of python

    # Simple dictionary
    d = {'k1': 'abc', 'k2': 123, 'k3': True, 'k4': [1,2,3]}
    # print('d = ',d)
    # print('type:', type(d))
    # print(d['k1'])

    # Common form of dictionary
    person = {
        'name': 'Theang Kosal',
        'age': 28,
        'gender': 'male',
        'employed': True,
        'birth place': 'Kandal',
    }

    print('Name     :', person['name'])
    print('Age      :', person['age'])
    print('Gender   :', person['gender'])
    print('Employed :', person['employed'])
    print('birth place :', person['birth place'])

    """
    # Dictionary Method
    d.clear()
    d.copy()
    d.fromkeys()
    d.get()
    d.items()
    d.keys()
    d.pop()
    d.popitem()
    d.setdefault()
    d.update()
    d.values()
    """



def list_of_dictionary():
    dataset = [
        {'name':'Kosal', 'age':28},
        {'name':'Veasna', 'age':29},
        {'name':'Vannak', 'age':30},
    ]

    for obj in dataset:
        print(f"My name is {obj['name']}. I am {obj['age']}.")




if __name__ == '__main__':
    os.system('clear')
    # lesson_range()
    # lesson_list()
    # lesson_tuple()
    # lesson_set()
    lesson_dictionary()
    # list_of_dictionary()
