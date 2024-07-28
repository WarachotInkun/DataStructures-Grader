class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self,head) -> None:
        self.head = head
        self.length =0
        self.tail =None

    def append(self,val):
        node = Node(val)
        if self.length ==0:
            
            self.head.next = node
            self.tail = node
            self.length+=1

        else:
            self.tail.next = node
            self.tail = self.tail.next
            self.length+=1
   


    def isEmpty(self):
        return self.length ==0
    

    def __str__(self) :
        if self.length == 0:
            return "List is empty"
        t = head.next 
        lst = []
        while t.next != None:
            lst.append(t.data)
            t =t.next
        lst.append(t.data)
        s = "->".join(lst)
        return f"link list : {s}"
    

    def insert(self, index, data):
        if index > self.length or index < 0 :
            return "Data cannot be added"
        t = self.head
        i = 0
        while i != self.length+1 :
            if i == index :
                newNode = Node(data)
                newNode.next = t.next
                t.next = newNode
                self.length += 1
                return f"index = {index} and data = {data}"
            else:
                t = t.next
                i+=1



        
a = input("Enter Input : ").split(",")
head = Node(None)
link = LinkedList(head)
node = [i for i in a[0].split(" ")]
for i in node:
    if i != "":
        link.append(i)
print(link)

for j in a[1:]:
    j = j.split(":")
    print(link.insert(int(j[0]),j[1]))
    print(link)
    