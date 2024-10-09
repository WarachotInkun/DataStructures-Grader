def insertion(lst1,lst2,index):

    if lst2 == [] :
        return lst1
    
    if lst1[index] > lst2[0] :
        if index == 0:
            lst1.insert(0,lst2[0])
            if  lst2[1:]!=[]:
                print(f"insert {lst2[0]} at index {index} : {lst1} {lst2[1:]}")
            else:
                print(f"insert {lst2[0]} at index {index} : {lst1}")
            return insertion(lst1,lst2[1:],len(lst1)-1)
        else:
            return insertion(lst1,lst2,index-1)
    
    else:
        lst1.insert(index+1,lst2[0])
        if lst2[1:]!=[]:
            print(f"insert {lst2[0]} at index {index+1} : {lst1} {lst2[1:]}")
        else:
            print(f"insert {lst2[0]} at index {index+1} : {lst1}")
        return insertion(lst1,lst2[1:],len(lst1)-1)
    

     









inp = list(map(int,input("Enter Input : ").split(" ")))

print(f"sorted\n{insertion([inp[0]],inp[1:],0)}")