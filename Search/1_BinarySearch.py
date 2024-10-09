def bi_search(l, r, arr, x):

    if r>=l :
        index = l+((r-l) // 2)
        if arr[index] == x :
            return True
        if x < arr[index]:
            return bi_search(0,index-1,arr,x)
        else:
            return bi_search(index+1,r,arr,x)
    else:
        return False


inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))