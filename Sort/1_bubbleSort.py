def bubble(lst):
    for n in range(len(lst)-1):
        swap = False
        temp =  None
        for i in range(len(lst)-n-1):
            if lst[i] > lst[i+1]  :
                temp = lst[i]
                swap = True
                lst[i] ,lst[i+1]  = lst[i+1],lst[i] 
                

        if not swap or len(lst)-n-1  ==1:
            print(f"last step : {lst} move[{temp}]")
            return
        else:
            print(f"{n+1} step : {lst} move[{temp}]")












inp = list(map(int,input("Enter Input : ").split(" ")))
bubble(inp)


