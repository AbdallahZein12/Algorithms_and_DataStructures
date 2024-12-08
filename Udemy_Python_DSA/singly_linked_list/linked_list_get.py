class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 
        
class LinkedList:
    def __init__(self,value):
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 
    
    def print_list(self):
        temp = self.head 
        while temp: 
            print(temp.value)
            temp = temp.next 
            
    def append(self,value): 
        new_node = Node(value=value)
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1 
        return True 

    def pop(self): 
        if self.length == 0: 
            return None 
        
        prev = self.head 
        temp = self.head 
        while temp.next: 
            prev = temp
            temp = temp.next 
            
        self.tail = prev 
        self.tail.next = None 
        self.length -= 1 
        if self.length == 0: 
            self.tail = None 
            self.head = None 
        return temp
    
    def prepend(self,value):
        new_node = Node(value=value)    
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head 
            self.head = new_node
        self.length += 1 
        return True 
    
    def pop_first(self):
        if self.length == 0: 
            return None 
        
        temp = self.head 
        self.head = self.head.next 
        temp.next = None 
        self.length -= 1 
        if self.length == 0: 
            self.tail = None 
        return temp 
        
    def get(self,index): 
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head 
        for _ in range(index):
            temp = temp.next 
        return temp
    
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)

ll.print_list()
print()

print(ll.get(0).value)
            
             
            