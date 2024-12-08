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
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
            
        self.length+=1 
        return True 
    
    def pop(self):
        if self.length == 0:
            return None 
        
        pre = self.head 
        temp = self.head 
        
        while temp.next:
            pre = temp 
            temp = temp.next 
        
        self.tail = pre 
        self.tail.next = None 
        self.length -= 1 
        if self.length == 0:
            self.head = None 
            self.tail = None 
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