a = input("Enter Input : ").split(",")
que = []
outQue =[]
for i in a:
    if i[0]=="E":
        s=""
        que.append(i[-1])
        if len(que)==1:
            s = que[0]
        else :
            s = ", ".join(que)
        print(s)
    elif i[0]=="D":
        if len(que)==0:
            print("Empty")
            continue
        temp = que.pop(0)
        if len(que)==1:
            s = que[0]
        elif len(que)==0:
             s = "Empty" 
        else :
            s = ", ".join(que)
        print(f"{temp} <- {s}")
        outQue.append(temp)

s=""
sq=""
if len(que)==1:
    s = que[0]
elif len(que)==0:
    s = "Empty"
else :
    s = ", ".join(que)


if len(outQue)==1:
    sq = outQue[0]
elif len(outQue)==0:
    sq = "Empty"
else :
    sq = ", ".join(outQue)
print(f"{sq} : {s}")