class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return 
        
        last_node = self.head 
        while last_node.next:
            last_node = last_node.next   
        last_node.next = new_node
        
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_after_node(self,prev_node,data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def delete_node(self, key):
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next
            
        if curr_node is None:
            return
        
        prev.next = curr_node.next
        curr_node = None
        
    
    def delete_node_at_pos(self,pos):
        curr_node = self.head
        
        if pos == 0:
            self.head = curr_node.next
            curr_node = None
            return
        
        prev = None
        count = 0
        while curr_node and count != pos:
            prev = curr_node
            curr_node = curr_node.next
            count += 1
        
        if curr_node is None:
            return
        
        prev.next = curr_node.next
        curr_node = None
        
    def len_iterative(self):
        count = 0
        curr_node = self.head
        
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count
    
    def len_recursive(self,node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)
        
        
        
        
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("E")
llist.insert_after_node(llist.head.next.next, "F")
llist.delete_node("B")
llist.delete_node_at_pos(1)
llist.print_list()
print(llist.len_iterative())
print(llist.len_recursive(llist.head))