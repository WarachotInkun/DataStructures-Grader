class Stack:
    def __init__(self):
        self.list = []
 
    def push(self,inp):
        self.list.append(inp)
 
    def pop(self):
        return self.list.pop()
 
    def last(self):
        if self.list != []:
            return self.list[-1]
 
def match(i1,i2):
    op = "(["
    cl = ")]"
    return op.index(i1) == cl.index(i2)
 
s = Stack()
str = input("Enter Input : ")
i = 0
err = 0
while i < len(str) and err == 0:
    if str[i] in "([":
        s.push(str[i])
    if str[i] in ")]":
        if s.list != []:
            if not match(s.pop(),str[i]):
                print("Parentheses : Unmatched ! ! !")
                err += 1
        else :
            print("Parentheses : Unmatched ! ! !")
            err += 1
    i += 1
if s.list == [] and err == 0:
    print("Parentheses : Matched ! ! !")
elif s.list != 0 and err == 0:
    print("Parentheses : Unmatched ! ! !")