a=[int(i) for i in input("Enter your List : ").split(",")]

def sort(n,list=[]):
    if n == 0 or n > (len(list)-1) :
        return
    if list[n]>list[n-1]:
        a.insert(n-1,a.pop(n))
        sort(n-1,list)
    sort(n+1,list)
    




sort(1,a)
print("List after Sorted :",a)