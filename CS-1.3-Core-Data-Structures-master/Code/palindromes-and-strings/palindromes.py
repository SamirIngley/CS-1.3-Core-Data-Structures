#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_recursive(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text, index = -1):
    # TODO: implement the is_palindrome function iteratively here

    for char in text:

        if not char.isalpha() or not text[index].isalpha():
            continue

        # print(char_index, text[index])
        # print('abs ', abs(index+1))
        # print(char, text[index])
        if len(text)//2 <= abs(index+1):
            return True
        
        if char.lower() == text[index].lower():
            index -= 1
        else:
            return False

    return True
    
        
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here

            
    if not left and not right:
        left = 0
        right = -1
    if left >= len(text)//2:
        return True
    else:
        while not text[left].isalpha():
            left += 1
        while not text[right].isalpha():
            right -= 1
        print(text[left], text[right])
        if text[left].lower() == text[right].lower():
            left += 1
            right -= 1
            return is_palindrome_recursive(text, left, right)
        else:
            return False
    return True
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
