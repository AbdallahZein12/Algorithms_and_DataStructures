class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 
        
class Stack: 
    def __init__(self, value):
        new_node = Node(value=value)
        self.top = new_node
        self.height = 1 
        
    def print_stack(self):
        temp = self.top 
        while temp: 
            print(temp.value)
            temp = temp.next 
        return  
    