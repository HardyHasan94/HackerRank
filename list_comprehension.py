# list comprehension problem,
# find all coordinates i,j,k such that i+j+k is not equal to not

 def lists(x,y,z,n):
    print(sorted([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]))