class Queue():

    def __init__(self):
        self.items = []
    
    def enQue(self, val):
        self.items.append(val)

    def deQue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def list(self):
        return self.items

myQue = Queue()
uQue = Queue()
a = input("Enter Input : ").split(",")

for i in a :
    i = i.split(" ")
    myQue.enQue(i[0])
    uQue.enQue(i[1])
point = 0
print("My   Queue = "+", ".join(myQue.list()))
print("Your Queue = "+", ".join(uQue.list()))

for i in range(len(myQue.list())):
    myAct =  myQue.list()[i][0]
    myLo =  myQue.list()[i][-1]
    uAct =  uQue.list()[i][0]
    uLo =  uQue.list()[i][-1]

    if myAct == uAct and myLo != uLo:
        point += 1
    elif  myAct != uAct and myLo == uLo:
        point += 2
    elif  myAct == uAct and myLo == uLo:
        point += 4
    elif  myAct != uAct and myLo != uLo:
        point -= 5
acDic = {"0":"Eat","1":"Game","2":"Learn","3":"Movie"} 
loDic = {"0":"Res.","1":"ClassR.","2":"SuperM.","3":"Home"}
mylist = [f"{acDic[myQue.list()[i][0]]}:{loDic[myQue.list()[i][-1]]}" for i in range(len(myQue.list())) ]
ulist = [f"{acDic[uQue.list()[i][0]]}:{loDic[uQue.list()[i][-1]]}" for i in range(len(uQue.list())) ]

print("My   Activity:Location = "+", ".join(mylist))
print("Your Activity:Location = "+", ".join(ulist))

if point >= 7:
    print(f"Yes! You're my love! : Score is {point}." )
elif point >= 0:
    print(f"Umm.. It's complicated relationship! : Score is {point}." )
else:
    print(f"No! We're just friends. : Score is {point}." )
    