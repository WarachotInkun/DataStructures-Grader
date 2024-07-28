class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        node = Node(item)
        if self.head ==None:
            self.head=node
            self.tail=self.head

        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail  = node



    def addHead(self, item):
        node = Node(item)
        if self.head ==None:
            self.head=node
            self.tail=self.head
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node


    def insert(self, pos, item):
        node =Node(item)
        count = 0 
        if pos == 0 :
            self.addHead(item)
            return
        if pos < 0:
            if abs(pos)>self.size():
                self.addHead(item)
                return    
            t = self.tail         
            while count != pos:
                t = t.previous
                count -= 1
            node.next = t.next
            node.previous = t
            t.next = node
            node.next.previous = node
        else:
            if pos > self.size():
                self.append(item)
                return
            t = self.head         
            while count != pos:
                t = t.next
                count += 1           
            node.next = t
            node.previous = t.previous
            t.previous.next = node
            t.previous = node
             



    def search(self, item):
        t = self.head
        while t != None:
            if t.value == item:
                return "Found"
            t = t.next
        return "Not Found"

    def index(self, item):
        t = self.head
        n = 0
        while t != None:
            if t.value == item:
                return n
            t = t.next
            n+= 1
        return -1

    def size(self):
        count = 0 
        lst = []
        if self.head == None:
            return 0
        else:
            t = self.head
            while t.next != None:
                count += 1
                t = t.next
                lst.append(t.value)
            count += 1
            s = " ".join(lst)
            return count
        
    def pop(self, pos):
        count = 0 
        if pos < 0:
            if self.size() == "Empty" or abs(pos) > self.size() or self.head == None:
                return  "Out of Range"  
            t = self.tail         
            while count != pos:
                t = t.previous
                count -= 1

        else:
            if self.size() == "Empty" or abs(pos) > self.size()-1 or self.head == None:
                return  "Out of Range"
            if pos == 0 :
                
                self.head.next = None
                self.head = None
                return  "Success"
            t = self.head         
            while count != pos:
                t = t.next
                count += 1
            if t.next != None:                        
                t.previous.next = t.next
                t.next.previous =t.previous
            else:
                t.previous.next = None
                   

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse()) 