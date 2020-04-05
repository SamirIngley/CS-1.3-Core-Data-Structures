#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    
    total = 0
    index = len(digits)

    if not digits or not base:
        return print("Please provide ('number', base) number as a string and base as an integer. ")

    # TODO: Decode digits from binary (base 2)
    if base == 2:
        # we are given digits which is a binary string
        # and want to return the number in base 10
        # convert each binary number to its respective base 10 value and add them all together
        # current 2 exponent is one more than whatever the previous exponent was!
        for num in digits:
            index -= 1
            if num == '1':
                # we want to add to our total: 2^ of whatever the index is  
                # print(index)
                place_value = 2**(index)
                # print('place_value: ', place_value)
                total += place_value
            elif num == '0':
                continue
            else:
                return print('not valid binary')

        return print('Base 2 total: ', total)

    # TODO: Decode digits from hexadecimal (base 16)
    elif base == 16:
        for num in digits:
            index -= 1
            place_value = 16**(index)

            value = 0
            if num not in string.hexdigits:
                # num needs to be a hex digit
                return print('not a valid hexadecimal')

            elif num not in string.digits:
                # num is a letter
                letter_value = 9
                for letter in string.ascii_lowercase:
                    letter_value += 1
                    if num.lower() == letter:
                        value = letter_value
                        break
            else:
                # num is a number
                value = int(num) 
            # print(num, place_value, value)
            total += place_value * value 

        return print('Base 16 total: ', total)
            
    # TODO: Decode digits from any base (2 up to 36)
    else:
        for num in digits:
            # digits is a string, num is a char
            index -= 1
            place_value = base**(index)

            if num not in string.digits:
                # num is a hex number
                letter_value = 9
                for letter in string.ascii_lowercase:
                    letter_value += 1
                    if num.lower() == letter:
                        value = letter_value
                        break
            else:
                # num is a number
                value = int(num) 
            # print(num, place_value, value)
            total += place_value * value 

        return print(f'Base {base} total: ', total)



def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    # number base 10 integer into base 2 integer. Return a string
    
    # 2 ** What_number is > 287

    # while number < 287:
    #     increase the degree of 2 by 1
    
    # record the previous degree 
    # subract 2 to the power of that degree from the number

    # REPEAT

    if base == 2:
        places = []

        number_copy = number 
        print(number, base)
        while number_copy > 0:
            value = 0
            degree = 0

            while value < number_copy:
                print('degree ',degree)
                value = 2 ** (degree)
                degree += 1

            print('value ', value)      

            if value == number_copy:
                # we landed on it
                places.append(degree-1)
                number_copy -= 2**(degree-1)
            else:
                # we crossed it
                places.append(degree-2)
                number_copy -= 2 ** (degree-2) 

            print('degree ',degree)
            print(2**(degree-2))
            print('new_num: ', number_copy)
            print('places ', places)

        binary_string = ''
        degree = 0
        for item in range(places[0] + 1):
            print(item)
            if item in places:
                binary_string += '1'
                # binary_string += 'item' + str(item) 
            else:
                binary_string += '0'
                # binary_string += 'item' + str(item)
            degree += 1
        
        bin_string = ''.join(reversed(binary_string))
        return(print(bin_string))

    # TODO: Encode number in hexadecimal (base 16)
    # if base == 16:
    #     quotient = number//16
    #     remainder = number%16
    #     if remainde
    # TODO: Encode number in any base (2 up to 36)
    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    # main()
    # decode('1001001', 2)
    # decode('A1B', 16)
    # decode('893', 36) 
    encode(482, 2)
