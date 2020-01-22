# This function returns the number of handshakes in a group of people

def handshake(n):
    #
    # Write your code here.
    #
    a = 0
    for i in range(n):
        a += i
    return a