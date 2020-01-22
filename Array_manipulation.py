# This returns the maximum element in an array.
# First create an array of length n where all elements are 0
# and then for each query, add a value to every element in a range.

def arrayManipulation(n, queries):
    res = [0]*(n+2)
    for que in queries:
        a = que[0]
        b = que[1]
        k = que[2]
        res[a]+=k
        res[b+1]-=k
    maximum = 0
    tot_sum = 0
    for val in res:
        tot_sum += val
        if maximum < tot_sum:
            maximum = tot_sum
    return maximum