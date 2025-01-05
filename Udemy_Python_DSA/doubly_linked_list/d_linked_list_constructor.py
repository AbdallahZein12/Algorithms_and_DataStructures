class Node:
    def __init__(self,value): 
        self.value = value 
        self.next = None 
        self.prev = None 
        
class DoublyLinkedList: 
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
            
        return 
    

my_list = DoublyLinkedList(2)
my_list.print_list()