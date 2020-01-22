# creating a staircase of height n of the character '#'

def staircase(n):
    for i in range(n):
        s = ' '
        s = (n-i-1)*s + (i+1)*'#'
        print(s)