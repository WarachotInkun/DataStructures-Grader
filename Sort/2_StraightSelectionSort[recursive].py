def find_max_index(arr, start, max_index):
    if start < 0:
        return max_index    
    if arr[start] > arr[max_index]:
        max_index = start   
    return find_max_index(arr, start -1, max_index)


def Selection(index,lst):
    if index <=  0:
        print(lst)
        return 
    
    max_ =find_max_index(lst,index,index)
    lst[index] ,lst[max_]  = lst[max_],lst[index] 
    if not index == max_:
        print(f"swap {lst[max_]} <-> {lst[index]} : {lst}")

    Selection(index-1,lst)
    

    







inp = list(map(int,input("Enter Input : ").split(" ")))

Selection(len(inp)-1,inp)
