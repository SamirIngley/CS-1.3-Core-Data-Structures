#!python
from math import floor

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
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # ASSUMING ARRAY IS SORTED
    # if the number exists it's between the first and last nums
    # found = False
    # new_array = array
    # mid_index = int(floor(len(new_array)/2)-1)

    # print(array)
    # print(item, item[0])
    # print(mid_index)
    # print(array[mid_index])
    # print(array[mid_index][0])

    # while not found:
        
    #     mid_index = int(floor(len(new_array)/2)-1)
    #     print('middex ', mid_index)


    #     if item == new_array[mid_index]:
    #         found = True
    #         print('found: ', item, new_array[mid_index])
    #         return mid_index 

    #     elif item[0] > new_array[mid_index][0]:
    #         new_array = new_array[mid_index:]
    #         print('item: ', item, item[0])
    #         print('array loc: ', new_array[mid_index])
    #         print('item is greater so.. ', new_array)

    #     elif item[0] < new_array[mid_index][0]:
    #         new_array = new_array[:mid_index]
    #         print('item: ', item, item[0])
    #         print('array loc: ', new_array[mid_index])
    #         print('item is less so.. ', new_array)
        
    #     elif len(new_array) == 1:
    #         found = True
    #         print('Not found: ', item, new_array[mid_index])
    #         return None
    

    new_array = array
    found = False
    may_exist = True
    letter = 0
    index = None

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
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

# binary_search([0], 0)