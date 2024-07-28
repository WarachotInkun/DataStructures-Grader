class Queue():

    def __init__(self):
        self.items = []
    
    def enQue(self, val):
        self.items.append(val)
    
    def enList(self,list):
        for i in list:
            self.items.append(i)

    def deQue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def list(self):
        return self.items




a = input("Enter Input (Normal, Mirror) : ").split(" ")

norQue = Queue()
mirQue = Queue()
norStack = [i for i in a[0]]
mirStack = [i for i in a[1]]



mirrorBomb = 0
normalBomb = 0
failBomb =0
fail = False
newStack = []

#++++++++++++++++++++++++++++++++++++#
while mirStack != []:
    newStack.append(mirStack.pop())
    if len(newStack) >= 3 and newStack[-1] == newStack[-2] == newStack[-3]:
        mirQue.enQue(newStack[-3])
        newStack.pop()
        newStack.pop()
        newStack.pop()
        mirrorBomb += 1

newNormal =[]
while norStack != []:
    newNormal.append(norStack.pop(0))
    if len(newNormal) >= 3 and newNormal[-1] == newNormal[-2] == newNormal[-3] and mirQue.list() != [] :
        temp = newNormal.pop() 
        temp2 = mirQue.deQue()
        newNormal.append(temp2)
        newNormal.append(temp)
        if temp==temp2:
            fail=True
            newNormal.pop()
            newNormal.pop()
            newNormal.pop()
            failBomb += 1

    if len(newNormal) >= 3 and newNormal[-1] == newNormal[-2] == newNormal[-3]:
        newNormal.pop()
        newNormal.pop()
        newNormal.pop()
        normalBomb += 1
        

#++++++++++++++++++++++++++++++++++++++#

print(f"NORMAL : \n{len(newNormal)}")
for i in list(reversed(newNormal)):
    print(i,end="")
if list(reversed(newNormal))==[]:
    print("Empty",end="")
print()

if not fail:
    print(f"{normalBomb} Explosive(s) ! ! ! (NORMAL)")
else:
    print(f"{normalBomb} Explosive(s) ! ! ! (NORMAL)\nFailed Interrupted {failBomb} Bomb(s)")

print("------------MIRROR------------")
print(f": RORRIM\n{len(newStack)}")
for i in list(reversed(newStack)):
    print(i,end="")
if list(reversed(newStack))==[]:
    print("ytpmE",end="")
print()
print(f"(RORRIM) ! ! ! (s)evisolpxE {mirrorBomb}")









