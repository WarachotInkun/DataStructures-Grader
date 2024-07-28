class Stack:
    def __init__(self):
        self.list = []
 
    def push(self,inp):
        self.list.append(inp)
 
    def pop(self):
        return self.list.pop()
 
    def size(self):
        return len(self.list)
 
    def __str__(self):
        return str(self.list)
 
s = Stack()
for i in input("Enter Input : ").split(","):
    if i[0] == "A":
        inp = int(i.split(" ")[1])
        print(f"Add = {inp}")
        s.push(int(inp))
    elif i == "P":
        if s.size() > 0:
            print(f"Pop = {s.pop()}")
        else:
            print("-1")
    elif i[0] == "D":
        inp = int(i.split(" ")[1])
        if s.size() != 0:
            t = Stack()
            for i in range(s.size()):
                num = s.pop()
                if num != inp:
                    t.push(num)
                else:
                    print(f"Delete = {inp}")
            for i in range(t.size()):
                s.push(t.pop())
        else:
            print("-1")
 
    elif i.split(" ")[0] == "MD":
        inp = int(i.split(" ")[1])
        if s.size() != 0:
            t = Stack()
            for i in range(s.size()):
                num = s.pop()
                if num <= inp:
                    t.push(num)
                else:
                    print(f"Delete = {num} Because {num} is more than {inp}")
            for i in range(t.size()):
                s.push(t.pop())
        else:
            print("-1")
 
    elif i.split(" ")[0] == "LD":
        inp = int(i.split(" ")[1])
        if s.size() != 0:
            t = Stack()
            for i in range(s.size()):
                num = s.pop()
                if num >= inp:
                    t.push(num)
                else:
                    print(f"Delete = {num} Because {num} is less than {inp}")
            for i in range(t.size()):
                s.push(t.pop())
        else:
            print("-1")
 
print(f"Value in Stack = {str(s)}")