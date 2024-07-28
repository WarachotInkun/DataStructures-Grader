class Queue():
    def __init__(self):
        self.items = []
    
    def enQue(self, val):
        self.items.append(val)

    def deQue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def list(self):
        return self.items

def encodemsg(q1, q2):
    que = [i for i in q2.list()]
    q1_list = q1.list()
    encoded_message = []

    for char in q1_list:
        temp = que.pop(0)
        
        if char.isupper():
            new_char = chr((ord(char) - 65 + temp) % 26 + 65)
        elif char.islower():
            new_char = chr((ord(char) - 97 + temp) % 26 + 97)
        
        que.append(temp)
        encoded_message.append(new_char)
    
    for char in encoded_message:
        q1.deQue()
        q1.enQue(char)
    
def decodemsg(q1, q2):
    que = [i for i in q2.list()]
    q1_list = q1.list()
    encoded_message = []

    for char in q1_list:
        temp = que.pop(0)
        
        if char.isupper():
            new_char = chr((ord(char) - 65 - temp) % 26 + 65)
        elif char.islower():
            new_char = chr((ord(char) - 97 - temp) % 26 + 97)
        
        que.append(temp)
        encoded_message.append(new_char)
    
    for char in encoded_message:
        q1.deQue()
        q1.enQue(char)

a = input("Enter String and Code : ").split(",")
s = [i for i in a[0] if i.isalpha()]
q1 = Queue()
q2 = Queue()

for i in s:
    q1.enQue(i)
for i in a[1]:
    q2.enQue(int(i))
encodemsg(q1, q2)
print(f"Encode message is :  {q1.list()}")
decodemsg(q1, q2)
print(f"Decode message is :  {q1.list()}")