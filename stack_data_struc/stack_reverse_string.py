from stack import Stack

def reverse_string(stack, input_str):
    # Loop through the string and push contents
    # character by character onto stack
    for i in range(len(input_str)):
        stack.push(input_str[i])
        
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
        
    return rev_str


stack = Stack()
input_str = "Hello"

print(reverse_string(stack=stack,input_str=input_str))