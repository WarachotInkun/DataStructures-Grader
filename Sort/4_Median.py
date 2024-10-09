
def bubble(lst1):
    lst = [i for i  in lst1] 
    for n in range(len(lst)-1):
        swap = False
        temp =  None
        for i in range(len(lst)-n-1):
            if lst[i] > lst[i+1]  :
                temp = lst[i]
                swap = True
                lst[i] ,lst[i+1]  = lst[i+1],lst[i] 
                

        if not swap or len(lst)-n-1  ==1:
            return lst
    return lst
    






l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "xxx"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    lst =[]
    l=list(map(int, l))

    for i in l :

        lst.append(i)
        s = bubble(lst)
        n = len(lst)
        index = (n-1) //2
        if n % 2:
            medain =  s[index]/1.0
        else:
            medain = (s[index]+s[index+1])/2.0


        print(f"list = {lst} : median = {medain}")

    