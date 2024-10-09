def bubble(l):
    for last in range(len(l)-1,0,-1):
        swaped = False
        for i in range (last):
            if l[i] > l[i+1]:
                l[i],l[i+1] = l[i+1],l[i]
                swaped = True
        if not swaped:
            break

def selection(l):
    for last in range(len(l)-1,0,-1):
        biggest = l[0]
        biggest_i = 0
        for i in range(1, last+1):
            if l[i] > biggest:
                biggest = l[i]
                biggest_i = i
        l[last],l[biggest_i] = l[biggest_i],l[last]

def insertion(l):
    for i in range(1,len(l)):
        iEle = l[i]
        for j in range(i, -1 ,-1):
            if iEle<l[j-1] and j>0:
                l[j] = l[j-1]
            else:
                l[j] = iEle
                break

def shell(l, dIncrements):
    for inc in dIncrements:
        for i in range(inc,len(l)):
            iEle = l[i]
            for j in range(i,-1,-inc):
                if iEle<l[j-inc] and j >= inc:
                    l[j] = l[j-inc]
                else:
                    l[j] = iEle
                    break

def mergeSort(l,left,right):
    center = (left+right)//2
    if left < right:
        mergeSort(l,left,center)
        mergeSort(l,center+1,right)
        merge(l,left,center+1,right)

def merge(l,left,right,rightEnd):
    start = left
    leftEnd = right -1
    result = []
    while left <= leftEnd and right <= rightEnd:
        if l[left] < l[right]:
            result.append(l[left])
            left +=1
        else:
            result.append(l[right])
            right +=1 
    while left <= leftEnd:
        result.append(l[left])
        left +=1
    while right<= rightEnd:
        result.append(l[right])

    for ele in result:
        l[start] = ele
        start += 1 
        if start > rightEnd:
            break

def quick(l,left,right):
    if left == right +1:
        if l[left] > l[right]:
            l[left], l[right] = l[right], l[left]
        return
    if left < right:
        pivot = l[left]
        i,j = left+1,right
        while i<j:
            while i<right and l[i]<=pivot:
                i += 1
            while j>left and l[j]>=pivot:
                j -= 1
            if i<j:
                l[i],l[j] = l[j],l[i]
        if left is not j:
            l[left] , l[j] = l[j],pivot
        quick(l,left,j-1)
        quick(l,j+1,right)
