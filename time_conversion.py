# convert 12 hour time to 24 hour format

def timeConversion(s):
    #
    # Write your code here.
    #
    if s[-2::1] == 'AM':
        s = s.replace('AM','')
        if s[:2]=='12':
            s = s.replace('12','00',1)
            return s
        else:
            return s
    s = s.replace('PM','')
    if s[:2]=='12':
        return s
    else:
        t = str(int(s[:2]) + 12)
        s = s.replace(s[:2], t, 1)
        return s