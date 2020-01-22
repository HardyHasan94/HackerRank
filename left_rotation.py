# This is a left rotation of an array a where d is a given number 
# indicating how many left rotations to be performed.

# The solution is as follow: 
# Find the element that will become the first element in the new rotated array. 
# That's the first line of code. 
# Next take the subarray starting from that element.
# Lastly extend that sunarray with the part that was removed from the original array.


d = d%len(a)
x = a[d:]
x.extend(a[:d])
for el in x:
    print(el, end = ' ')