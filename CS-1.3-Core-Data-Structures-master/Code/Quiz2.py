# write a function that reverses an integer using a stack and returns it as an integer
# for example, if your input number is 3479 the function will return 9743. 

def stack_reverse(input_num):

    stack = []
    reverse = ''


    for item in str(input_num):
        stack.append(item)
    # print(stack)

    for num in range(len(stack)):
        reverse += stack.pop()

    print(f'Input: {input_num} -- Reversed with stack: {reverse}')
    return int(reverse)

input_int = 3479
stack_reverse(input_int)