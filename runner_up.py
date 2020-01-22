# find the runner_up score in a list of scores

def runner_up(n,array):
    array = sorted(array,reverse=True)
    while len(array)>0:
        x = array.pop(0)
        if x != array[0]:
            print(array[0])
            break