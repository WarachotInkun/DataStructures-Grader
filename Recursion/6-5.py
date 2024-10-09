def staircase(n,s):
    if s ==0:
        print("Not Draw!")
    if n > 0:        
        print("_"*(n-1)+"#"*(s-(n-1)))
        staircase(n-1,s)
    elif n < 0:   
        print("_"*(n+s)+"#"*abs(n))
        staircase(n+1,s)
    
        



a=int(input("Enter Input : "))
staircase(a,abs(a))