class Node:
    def __init__(self,value):
        self.value = value
        self.next = None 
        
class LinkedList:
    def __init__(self,value=None):
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = None 
        
    def print_list(self):
        temp = self.head 
        while temp:
            print(temp.value)
            temp = temp.next 
            

ll = LinkedList(value=5)
ll.head.next = Node(value=15)
ll.head.next.next = Node(value=17)
ll.print_list()