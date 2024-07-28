class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.status = None
 
inp = input("Enter edges: ").split(",")
 
nodeList = []
intersection = []
linkHead = []
for i in range(len(inp)):
    this, next = inp[i].split(">")
    nlstv = [nodeList[i].value for i in range(len(nodeList))]
    if this not in nlstv:
        thisNode = Node(this)
        nodeList.append(thisNode)
    if next not in nlstv:
        nextNode = Node(next)
        nodeList.append(nextNode)
 

 
for i in range(len(inp)):
    thisNode = nextNode = None
    this, next = inp[i].split(">")
 

    for item in nodeList:
        if item.value == this:
            thisNode = item
            break 

    for item in nodeList:
        if item.value == next:
            nextNode = item
            break  

    if thisNode:
        thisNode.next = nextNode
 

 
 
for i in range(len(nodeList)):
    for j in range(len(nodeList)):
        if i != j and nodeList[j].next != None and nodeList[i].next != None and nodeList[i].next.value == nodeList[j].next.value:
            if nodeList[i].next.value not in [node.value for node in intersection]:
                intersection.append(nodeList[i].next)
size = []
if len(intersection) <= 0:
    print("No intersection")
    status = 'no'
else:
    for node in intersection:
        count = 0
        temp = node.value
        nlst = [nodeList[i].next for i in range(len(nodeList))]

        memory = []
        while node is not None and node.value not in memory:
            memory.append(node.value)
            count += 1
            node = node.next

        size.append(f"Node({temp}, size={count})")
 
size.sort()
for i in size:
    print(i)
 
if len(intersection) > 0:
    for node in intersection:
        count = 0
        temp = node.value
        nlst = [nodeList[i].next for i in range(len(nodeList))]
        memory = []
        while node is not None and node.value not in memory:
            memory.append(node.value)
            count += 1
            node = node.next
 
        for item in nodeList:
            if item.next != None and item.next.value == temp:
                item.next = None
 

 
for item in intersection:
    nodeList.remove(item)
 

for i in range(len(nodeList)):
    nodeList[i].status = "head"
    for j in range(len(nodeList)):
        if nodeList[j].next != None and nodeList[i].value == nodeList[j].next.value:
            nodeList[i].status = "body"
            break
    if nodeList[i].status == "head":
        linkHead.append(nodeList[i])
linkHead.sort(key = lambda a: a.value)

lst = []
for node in linkHead:
    new = []
    while node != None:
        new.append(node.value)
        node = node.next
    lst.append(new)

ans = []
while lst != []:
    for  i in lst:
        if i != []:
            ans.append(i.pop(0))
        else:
            lst.remove(i)
 
if len(intersection) > 0:
    print("Delete intersection then swap merge:")
    print(" -> ".join(ans))