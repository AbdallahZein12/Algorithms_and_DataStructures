class Node: 
    def __init__(self, value):
        self.value = value 
        self.next = None 
        
    
class LinkedList:
    def __init__(self, value):
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 
        
    def print_list(self):
        temp = self.head 
        while temp: 
            print(temp.value)
            temp = temp.next 
            
    def append(self, value):
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
            self.head = None 
            self.tail = None 
        return temp  
    
    def prepend(self, value):
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
    
    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None 
        
        temp = self.head 
        for _ in range(index):
            temp = temp.next 
        
        return temp 

    def set_value(self, index, value):
        temp = self.get_value(index=index)
        if temp:
            temp.value = value
            return True 
        return False 

    def insert(self, index, value):
        # temp = self.get_value(index=index)
        # if temp: 
        #     temp_next = temp.next
        #     new_node = Node(value=value)
        #     temp.next = new_node
        #     new_node.next = temp_next
        #     return True 
        # return False
        
        if index < 0 or index > self.length:
            return False 
        if index == 0:
            return self.prepend(value=value)
        if index == self.length:
            return self.append(value=value)
        new_node = Node(value=value)
        temp = self.get_value(index-1)
        new_node.next = temp.next 
        temp.next = new_node
        self.length += 1 
        return True 
    
    
        
        

ll = LinkedList(15)
ll.append(20)
ll.append(23)
ll.print_list()
