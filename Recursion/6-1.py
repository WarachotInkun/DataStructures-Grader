

def fac(n):    
    if n <2:
        return 1
    

    return n*fac(n-1)



a=int(input("Enter Number : "))
print(f"{a}! = {fac(a)}")