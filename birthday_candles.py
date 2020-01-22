# this array contains values representing heights. 
# the function returns the number of elements with max value

def birthdayCakeCandles(ar):
    ar = sorted(ar)
    i = ar.index(max(ar))
    return len(ar)-i