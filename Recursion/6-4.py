A = []
B = []
C = []
rods = [A,B,C]
lists ={"A":A,"B":B,"C":C}

def move(n, source_name, destination_name):
    source = lists[source_name]
    destination = lists[destination_name]
    if source:
        destination.append(source.pop(-1))
        print(f"move {n} from  {source_name} to {destination_name}")

def display():
    n = len(A)+len(B)+len(C)+1
    for i in range(n,0,-1):
        for rod in rods:
            if len(rod)>=i:
                print(rod[i-1],end="  ")
            else:
                print("|",end="  ")
        print()        

def TowerOfHanoi(n , source, destination, helper):
    if n==1:
        move(1,source,destination)
        display()
        return
    TowerOfHanoi(n-1, source, helper, destination)
    move(n,source,destination)
    display()
    TowerOfHanoi(n-1, helper, destination, source)
         

n = int(input("Enter Input : "))


for i in range(n,0,-1):
    A.append(i)

display()
TowerOfHanoi(n,'A',"C","B") 



