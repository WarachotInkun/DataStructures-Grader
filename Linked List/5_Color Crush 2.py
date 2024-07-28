class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
 
class Linklist:
    def __init__(self):
        self.head = None
        self.length = 0
 
    def addLast(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else :
            current_node = self.head
 
            while current_node.next != None:
                current_node = current_node.next
 
            current_node.next = new_node
            new_node.prev = current_node
        self.length += 1
 
    def deleteNode(self,node):
        if node == self.head:
            return
        del_data = node.data
        prev_node = node.prev
        if node.next != None:
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
        else : prev_node.next = None
        node.data = None
        node.prev = None
        node.next = None
        self.length -= 1
        return del_data
 
    def displayList(self):
        current_node = self.head
        snake_child = []
        while current_node != None:
            snake_child.append(str(current_node.data))
            current_node = current_node.next
        if len(snake_child) > 1:
            display = f'({snake_child[0]})->' + '->'.join(snake_child[1:])
        else : display = f'({snake_child[0]})->Empty'
        print(display)
 
    def initialize(self, ls):
        self.head = None
        self.length = 0
 
        ls_snake = ls.split()
        for ele in ls_snake:
            self.addLast(int(ele))
 
        self.displayList()
 
    def sw(self):
        counter = 0
        current_node = self.head.next
        while current_node != None and current_node.next != None:
            current_node.data, current_node.next.data = current_node.next.data, current_node.data
            current_node = current_node.next.next
            counter += 2
 
        if counter % 2 == 0 and current_node != None:
            self.deleteNode(current_node)
 
        print('Swap success!')
        self.displayList()
        print('------------------------------')
 
    def sh(self):
        sh_list = []
        current_node = self.head
        while current_node != None:
                if current_node.data > self.head.data:
                    current_node = current_node.prev
                    sh_list.append(self.deleteNode(current_node.next))
                current_node = current_node.next
 
        print(f'Shake success!->{sh_list}')
        self.displayList()
        print('------------------------------')
 
    def f(self,data):
        self.addLast(int(data))
 
        print(f'Steal success!->{data}')
        self.displayList()
        print('------------------------------')
 
    def d(self, target):
        target = int(target)
        current_node = self.head
        weight = 0
        d_list = []
 
        while current_node != None:
            weight += current_node.data
            last_node = current_node
            current_node = current_node.next
 
        if weight < target:
            current_node = last_node
            while current_node != None and current_node != self.head:
                if current_node.data != 0 and target % current_node.data == 0:
                    while current_node.next:
                        d_list.append(self.deleteNode(current_node.next))
                    break
                current_node = current_node.prev
 
            if d_list == []:
                if last_node.data == 0:
                    self.head.data, last_node.data = last_node.data, self.head.data
                elif target % last_node.data != 0 :
                    self.head.data, last_node.data = last_node.data, self.head.data
 
        print(f'Play success!->{d_list}')
        self.displayList()
        print('------------------------------')
 
    def start(self, strng):
        while True:
            snake_child, operations = strng.split('/')
            self.initialize(snake_child)
            self.operation(operations)
            strng = input('Snake Game : ')
 
    def end(self):
        if self.length == 1:
            print('Mom is dead')
            return True
        return False
 
    def operation(self, ls):
        operations = ls.split(',')
        for operation in operations:
 
            if self.end():
                return
 
            if operation.startswith('F'):
                i, data = operation.split()
                self.f(data)
            elif operation.startswith('D'):
                i, target = operation.split()
                self.d(target)
            elif operation == 'SW':
                self.sw()
            elif operation == 'SH':
                self.sh()
        self.end()
 
snake = Linklist()
snake.start(input('Snake Game : '))