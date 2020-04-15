# Quiz 1 Question 5
# Write a function called compute_sum() that takes in a
# single integer argument n and returns the sum of the positive
# integers from 1 to n. For example compute_sum(4) would return 10,
# or 1+2+3+4. You need to use a loop to complete this funciton. 

def compute_sum(num):
    total = 0
    for i in range(num+1):
        # print(i)
        total += i
    # print('total: ', total)
    return total

compute_sum(4)
compute_sum(10)