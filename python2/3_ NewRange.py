num1 = input("*** New Range ***\nEnter Input : ").split()



def  range(*args):
    start = 0
    stop = 1
    step  = 1
    lst = []
    if len(args[0]) == 1:
        stop = args[0][0]
    elif len(args[0]) == 2:
        start = args[0][0]
        stop = args[0][1]
    elif len(args[0]) == 3:
        start = args[0][0]
        stop = args[0][1]
        step = args[0][2]
    start = float(start)
    stop = float(stop)
    step = float(step)

    while start <stop:
        lst.append(round(start, 3))
        start+=step
    return(lst)
tup = tuple(range(num1))
print(tup)

