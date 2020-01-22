# return absolute value of the differnce of the main diagonals of a matrix.

def diagonalDifference(arr):
    # Write your code here
    res = 0
    for i in range(len(arr)):
        res += arr[i][i]-arr[i][len(arr)-i-1]
    return abs(res)