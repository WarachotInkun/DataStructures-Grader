class Queue():

    def __init__(self):
        self.items = []
    
    def enQue(self, val):
        self.items.append(val)

    def enLeftQue(self, val):
        self.items.insert(0,val)

    def deQue(self):
        return self.items.pop(0)
    
    def left(self,temp = 0):
        return self.items[temp]
    
    def insert(self,index,val):
        self.items.insert(index,val)
    
    def isEmpty(self):
        return self.items == []
    
    def list(self):
        return self.items


que= Queue()
queS = Queue()
a = input("Enter Input : ").split(",")
for i in a:
    i = i.split(" ")
    if "EN" in i[0] :
        que.enQue(i[-1])
    elif "ES" in i[0] :
        queS.enQue(i[-1])                        

    elif "D" in i[0]:
        if queS.list() == [] and que.list() == []:
            print("Empty")
        elif queS.list() != []:
            print(queS.deQue())
        else:
            print(que.deQue())




