# Function to find the number of a given string in an array of strings 

def matchingStrings(strings, queries):
    a = []
    for que in queries:
        i = 0
        for st in strings:
            if st == que:
                i+=1
        a.append(i)
    return a