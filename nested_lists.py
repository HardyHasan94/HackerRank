# Given the names and grades for each student in a Physics class of N 
# students, store them in a nested list and print the name(s) of 
# any student(s) having the second lowest grade

# a is the array

a = sorted(a, key = lambda kv: kv[1])
a = [e for e in a if e[1] != a[0][1]]
a = sorted([e for e in a if e[1] == a[0][1]])
for element in a:
    print(element[0])