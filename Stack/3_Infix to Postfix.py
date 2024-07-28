class Stack():
    def __init__(self) -> None:
        self.item = []

    def push(self, val):
        self.item.append(val)

    def pop(self):
        return self.item.pop()

    def top(self):
        return self.item[-1]

    def isEmpty(self):
        return self.item == []

s = input("Enter Infix : ")
lst = ["+", "-", "/", "*", "^"]
dic = {"+": 1, "-": 1, "/": 2, "*": 2, "(": 0, ")": 0, "^": 3}
stack = Stack()
output = Stack()

for i in s:
    if i in dic.keys():
        if i == ")":
            while not stack.isEmpty() and stack.top() != "(":
                output.push(stack.pop())
            stack.pop()
            continue
        if i == "(" or stack.isEmpty() or dic[stack.top()] < dic[i]:
            stack.push(i)
        else:
            while not stack.isEmpty() and dic[stack.top()] >= dic[i]:
                output.push(stack.pop())
            stack.push(i)
    else:
        output.push(i)

while not stack.isEmpty():
    output.push(stack.pop())


result = []
while not output.isEmpty():
    result.append(output.pop())

print("Postfix :", ''.join(result[::-1]))





