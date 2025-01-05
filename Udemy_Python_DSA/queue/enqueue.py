class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class Queue:
    def __init__(self, value):
        new_node = Node(value=value)
        self.first = new_node
        self.last = new_node
        self.height = 1 
        
    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next 
        return 
    
    def enqueue(self, value):
        new_node = Node(value=value)
        if self.height == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.height += 1 
        return True 