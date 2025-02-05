class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
        
    def insert_at_start(self,value):
        temp = self.head
        self.head =  Node(value)
        self.head.next = temp
        
        self.length += 1
    
    def remove_from_start(self):
        if self.length == 0:
            self.head = None
            self.tail = None
            
        else:
            self.temp = self.head.next
            self.head.next = None
            self.head = self.temp
            self.length -= 1
        
    def print_linklist(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self,value):
        temp = Node(value)
        if self.length == 0:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = self.tail.next
        self.length  += 1
        
    def remove_from_last(self):
        temp = self.head
        if self.length == 0:
            return print('no element to remove')
        
        count = 0

        while temp.next and temp.next.next:
            temp = temp.next
            count += 1
        
        temp.next = None
        self.tail = temp
        self.length -= 1
                
                    
                    
        
l = LinkedList(4)
l.insert_at_start(123)
l.append(90)
l.append(91)
l.append(92)

l.remove_from_last()

l.print_linklist()