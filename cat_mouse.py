# find out which cat catches the mouse

def catAndMouse(x, y, z):
    d1 = abs(z-x)
    d2 = abs(z-y)
    if d1<d2:
        return('Cat A')
    elif d1>d2:
        return('Cat B')
    else:
        return('Mouse C')