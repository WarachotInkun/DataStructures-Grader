num = [*map(int,input("*** Fun with countdown ***\nEnter List : ").split())]
lst = []
i = 0 
while i < len(num):
    if i != len(num)-1:
        if num[i]-num[i+1]== 1:
            newLst = []
            j = i
            while num[j] -num[j+1] == 1:
                newLst.append(num[j])
                j+=1
                if j == len(num)-1:
                    break
            newLst.append(num[j])
            i = j
            lst.append(newLst)
        elif num[i]-num[i+1]!= 1 and num[i] ==1:
            lst.append([1])
    else:
        if num[i]-num[i-1]!= -1 and num[i] == 1:
            lst.append([1])      
    i+=1


for i in lst:
    if min(i) !=1 :
        lst.remove(i)
lst= [len(lst),lst]
print(lst)

