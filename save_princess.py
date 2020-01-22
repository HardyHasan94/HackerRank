# AI problem
# save the princess being stuck in a corner of a matrix

def directions(m,d1,d2):
    for i in range(m):
        print(d1)
        print(d2)

def displayPathtoPrincess(n,grid):
    half = (int(n)-1)//2
    if(ord(grid[0][0]) == ord('p')):
        directions(half,'UP', 'LEFT')
    elif ord(grid[m-1][0]) == ord('p'):
        directions(half,'DOWN','LEFT')
    elif ord(grid[0][m-1]) == ord('p'):
        directions(half,'UP','RIGHT')
    else:
        directions(half, 'DOWN','RIGHT')