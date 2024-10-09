def find_max_index(arr, start, min_index):
    if start < 0:
        return min_index
    
    if arr[start] > arr[min_index]:
        min_index = start
    
    return find_max_index(arr, start -1, min_index)


def Selection(index,lst):
    if index <=  0:
        print(lst)
        return 
    
    min_ =find_max_index(lst,index,index)
    lst[index] ,lst[min_]  = lst[min_],lst[index] 
    if not index == min_:
        print(f"swap {lst[min_]} <-> {lst[index]} : {lst}")

    Selection(index-1,lst)
    

    







inp = list(map(int,input("Enter Input : ").split(" ")))

Selection(len(inp)-1,inp)
