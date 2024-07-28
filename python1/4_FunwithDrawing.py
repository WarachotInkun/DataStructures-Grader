num = int(input("*** Fun with Drawing ***\nEnter input : "))


for  i in range(-((num-1)*2),((num-1)*2)+1):
    for j in range(-((num-1)*2),((num-1)*2)+1):
        if max(abs(j),abs(i)) % 2== 0:
            print("#",end="")
        else:
            print(".",end="")
    print("")