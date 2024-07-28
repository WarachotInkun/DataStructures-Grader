class Stack:
    def __init__(self):
        self.stack = []
 
    def push(self, item):
        self.stack.append(item)
 
    def pop(self):
        self.stack.pop()
 
s = Stack()
 
 
inp = input('Enter Input : ').split(',')
for item in inp:
    if item.split(" ")[0] == 'A':
        h = int(item.split(" ")[1])
        if len(s.stack) > 0 and h >= s.stack[-1]:
            for num in reversed(s.stack):
                if h>=num:
                    s.stack.pop()
            s.push(h)
        else:
            s.push(h)
    elif item == 'B':
        print(len(s.stack))