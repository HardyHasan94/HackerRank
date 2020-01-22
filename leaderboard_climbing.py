# this returns an array of Alice rankings after each game she play.

def upper_elements(l, element,index):
    i = index
    for el in l:
        if element >= el:
            return i
        else:
            i+=1
    return i

def climbingLeaderboard(scores, alice):
    keys = []
    for el in scores:
        if el not in keys:
            keys.append(el)
    rest = []
    x = len(keys)//2

    for el in alice:
        if el > keys[len(keys)-x]:
            i = upper_elements(keys, el,1)
            rest.append(i)
        else:
            if x%2==1:
                i = upper_elements(keys[x+1:],el,len(keys)-x+1)
                rest.append(i)
            else:
                i = upper_elements(keys[x:],el,len(keys)-x)
                rest.append(i)
    return rest