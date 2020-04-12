#!python
from math import floor, ceil

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if index == len(array):
        return None
    elif array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index+1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # ASSUMING ARRAY IS SORTED

    new_array = array
    found = False
    may_exist = True
    letter = 0

    while not found and may_exist:

        middle = int(floor(len(new_array)/2 - 1))
        print(middle, item, new_array[middle], item[0], new_array[middle][0], new_array)

        if new_array[middle] == item:
            print('found it', item, new_array[middle], new_array)
            found = True
            return array.index(item) 
        
        elif len(new_array) == 1 and new_array[0] != item:
            print('out of items, no luck')
            may_exist = False
            return None
        
        elif item[letter] == new_array[middle][letter]:
            letter += 1
            print('moved letter')
            
        elif new_array[middle][letter] < item[letter]:
            new_array = new_array[middle+1:]
            letter = 0
            print('item is greater')
            print(new_array)
        
        elif new_array[middle][letter] > item[letter]:
            new_array = new_array[:middle+1]
            letter = 0
            print('item is less')
            print(new_array)

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    letter = 0

    if not left and not right:
        left = 0
        right = len(array)-1

    middle = left + int(ceil((right-left)/2))
    if item == array[middle]:
        print('middle ', middle)
        print('found: ', item, array[middle], right, left)
        return array.index(array[middle])
    elif right-left == 0:
        print('dne')
        return 
    
    print(array[middle])
    while item[letter] == array[middle][letter]:
        letter += 1
        print('letter up')

    if item[letter] > array[middle][letter]:
        print(item, item[letter], 'item is greater than ', array[middle], array[middle][letter])
        left = middle
        print('left = middle', middle)
        print('right ', right)
        binary_search_recursive(array, item, left, right)
    elif item[letter] < array[middle][letter]:
        print(item, item[letter], 'item is less than ', array[middle], array[middle][letter])
        right = middle
        print('right = middle', middle)
        print('left ', left)
        binary_search_recursive(array, item, left, right) 
        






    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

binary_search(['alex', 'banana', 'cab', 'top', 'weird', 'zoo'], 'zoo')