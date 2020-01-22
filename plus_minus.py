# in an array, find the fraction of positive elements, negatives and zeros.

def plusMinus(arr):
    p = 0
    n = 0
    z = 0
    l = len(arr)
    for el in arr:
        if el>0:
            p +=1
        elif el<0:
            n+=1
        else:
            z+=1
    print(round(p/l,6))
    print(round(n/l,6))
    print(round(z/l,6))