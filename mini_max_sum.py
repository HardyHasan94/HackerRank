# in a  array of five elements, 
# find the minimum and maximum sum of exactly four elements

def miniMaxSum(arr):
    max = 0
    min = 0
    arr = sorted(arr)
    for el in arr[:4]:
        min+=el
    for el in arr[1:]:
        max+=el
    print(min,max)