# solution to find the max sum of hourglass in an array

def hourglassSum(arr):
    sums = []
    for i in range(4):
        for j in range(4):
            s = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            sums.append(s)
    return max(sums)