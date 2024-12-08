class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 
        
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 
        
    def print_list(self):
        temp = self.head 
        print("LinkedList:")
        while temp:
            print(temp.value)
            temp = temp.next 
            
    def append(self,value):
        new_node = Node(value=value)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head, self.tail = new_node
        
        self.length += 1 
        return True
            
ll = LinkedList(15)
ll.print_list()
ll.append(16)
ll.print_list()
ll.append(17)
ll.print_list()
ll.append(18)
ll.print_list()
        