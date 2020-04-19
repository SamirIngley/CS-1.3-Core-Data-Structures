#!python
from collections import deque


def contains(text, pattern, index=0):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)

    my_deque = deque([None for i in range(len(pattern))]) # create an array of None values the size of the pattern
    # print(my_deque)

    for char in text:   # loop through the whole text
        my_deque.append(char)   # add to the deque the next char
        my_deque.popleft()  # remove the previous char 
        # print(my_deque) # <--- enable this statement to see the deque in action

        index = 0   # reset the index every loop, bc we need to check from the beginning of the pattern 
        while index < len(pattern) and pattern[index] == my_deque[index]:   # while they match and we're not at the end of the pattern
            # print(pattern[index], my_deque[index]) # <--- enable this to see valid the comparisons
            index += 1  # go to the next index for both the pattern and the deque

        # print(pattern[index], my_deque[index]) # <--- enable this to see a comparison that broke the loop the comparisons
        # we've exited the loop for one of two reasons
        if index == len(pattern):   # if the index matches the length of the array - the pattern exists. The while loop broke because there were no more letters in the pattern to match 
            # print('Woohoo!')
            return True
        else:   # if the index did not match the length of the pattern, the while loop broke early - so start over!
            # print('Nope!')
            continue
    return False

# SAME AS CONTAINS, JUST RETURNING INDEX INSTEAD        
def find_index(text, pattern, index=0):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    my_deque = deque([None for i in range(len(pattern))]) # create an array of None values the size of the pattern
    # print(my_deque)

    threshold = 0
    index_in_text = 0
    for char in text:   # loop through the whole text

        my_deque.append(char)   # add to the deque the next char
        my_deque.popleft()  # remove the previous char 
        # print(my_deque) # <--- enable this statement to see the deque in action

        index = 0   # reset the index every loop, bc we need to check from the beginning of the pattern 
        while index < len(pattern) and pattern[index] == my_deque[index]:   # while they match and we're not at the end of the pattern
            # print(pattern[index], my_deque[index]) # <--- enable this to see valid the comparisons
            index += 1  # go to the next index for both the pattern and the deque

        if threshold < len(pattern):
            threshold += 1
        # print(pattern[index], my_deque[index]) # <--- enable this to see a comparison that broke the loop the comparisons
        # we've exited the loop for one of two reasons
        if index == len(pattern):   # if the index matches the length of the array - the pattern exists. The while loop broke because there were no more letters in the pattern to match 
            # print('Woohoo!')
            return index_in_text
        else:   # if the index did not match the length of the pattern, the while loop broke early - so start over!
            # print('Nope!')
            if threshold == len(pattern):
                index_in_text += 1


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)

    index_list = []

    my_deque = deque([None for i in range(len(pattern))]) # create an array of None values the size of the pattern
    # print(my_deque)
    
    threshold = 0
    index_in_text = 0
    for char in text:   # loop through the whole text

        my_deque.append(char)   # add to the deque the next char
        my_deque.popleft()  # remove the previous char 
        # print(my_deque) # <--- enable this statement to see the deque in action            

        index = 0   # reset the index every loop, bc we need to check from the beginning of the pattern 
        while index < len(pattern) and pattern[index] == my_deque[index]:   # while they match and we're not at the end of the pattern
            # print(pattern[index], my_deque[index]) # <--- enable this to see valid the comparisons
            index += 1  # go to the next index for both the pattern and the deque

        if threshold < len(pattern):
            threshold += 1

        # print(pattern[index], my_deque[index]) # <--- enable this to see a comparison that broke the loop the comparisons
        # print(f'threshold count: {threshold}/{len(pattern)}', 'index being comapred: ', index_in_text, 'char in text: ', char)
        # we've exited the loop for one of two reasons
        if index == len(pattern):   # if the index matches the length of the array - the pattern exists. The while loop broke because there were no more letters in the pattern to match 
            # print('Woohoo!')
            index_list.append(index_in_text)
            index_in_text += 1
            # print(index_list)
        else:   # if the index did not match the length of the pattern, the while loop broke early - so start over!
            # print('Nope!')
            if threshold == len(pattern):
                index_in_text += 1
        
    return index_list


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
