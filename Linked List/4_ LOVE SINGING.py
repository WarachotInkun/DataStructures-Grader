class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next
 
 
class LinkList:
    def __init__(self):
        self.head = None
 
    def appendHead(self,value):
        node = Node(value,self.head)
        self.head = node
 
    def appendLast(self,value):
        if self.head is None:
            self.appendHead(value)
            return
        else:
            n = Node()
            n.value = value
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = n
 
    def removeLast(self):
        if self.head == None : 
            print("Error!!!")
            return
        if self.head.next == None:
            self.head = None
            return
        else:
            p = self.head
            while p.next.next != None:
                p=p.next
            p.next = p.next.next
 
    def rename(self, newName):
        if(self.head != None):
            self.removeLast()
            self.appendLast(newName)
        else:
            print("Error!!!")
 
    def printList(self):
        t = self.head
        if(t == None):
            print("Linklist is empty!",end='')
        while t != None:
            print(t.value , end='')
            if t.next != None:
                print(" -> ",end='')
            t = t.next
        print("")
        #CODE HERE
 
    def printListWithNoDuplicate(self):
        seen_values = set()
        current = self.head
        if(current == None):
            print("Linklist is empty!",end='')
        first = True 
        while current:
            if current.value not in seen_values:
                seen_values.add(current.value)
                if not first:
                    print(" -> ", end='')
                print(current.value, end='')
                first = False
            current = current.next
        print("")
 
    def operator(self,list):
        for l in list:
            if(l[0] == "A"):
                self.appendLast(l.split()[1])
            elif(l[0]=="R"):
                self.rename(l.split()[1])
            elif(l[0]=="D"):
                self.removeLast()
            else:
                print("Error!!!")
 
 
def convertToLinkList(ls):
    ls_result = LinkList()
    for data in ls:
        ls_result.appendLast(data)
    return ls_result
 
 
print("*** My Favourite Keynote ***")
inputl = input("Enter Input / List of operation : ").split('/')
listSong = [ele for ele in inputl[0].strip().split(' ')]
operations = [ele for ele in inputl[1].strip().split(", ")]
 
myLinkList = convertToLinkList(listSong)
myLinkList.printList()
myLinkList.operator(operations)
myLinkList.printList()
myLinkList.printListWithNoDuplicate()