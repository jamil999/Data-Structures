class Stack_in_array:
    my_stack = []
    point = - 1
        
    def push(self, char):
        self.my_stack = self.my_stack + [char]
        self.point = self.point + 1
        
    def pop(self):
        store = self.my_stack[self.point]
        self.my_stack = self.my_stack[:-1]
        self.point = self.point - 1
        return store
        
    def peek(self):
        return self.my_stack[self.point]

def parenthesis_checker_in_array(expression):
    
    paren_stack = Stack_in_array()
    index_stack = Stack_in_array()
    opening = ['(','{','[']
    ending = [')','}',']']
    size = len(expression)
    spinner = 0
    
    while spinner < size:
        if expression[spinner] in opening:
            paren_stack.push(expression[spinner])
            index_stack.push(spinner)
        
        if expression[spinner] in ending:
            
            if len(paren_stack.my_stack) != 0:
                see = paren_stack.peek()
                
                if see == '(' and expression[spinner] == ')':
                    paren_stack.pop()
                    index_stack.pop()
                    
                if see == '{' and expression[spinner] == '}':
                    paren_stack.pop()
                    index_stack.pop()
                    
                if see == '[' and expression[spinner] == ']':
                    paren_stack.pop()
                    index_stack.pop()
                    
            elif len(paren_stack.my_stack) == 0:
                
                print(expression)
                print('This expression is NOT correct.')
                print('Error at character #'+str(spinner+1)+'.'+"'"+str(expression[spinner])+"'"+'- not opened.\n')
                return
                  
        spinner = spinner + 1
   
    if len(paren_stack.my_stack)==0:
        print(expression)
        print('This expression is correct.\n')
        
    else:
        print(expression)
        print('This expression is NOT correct.')
        print('Error at character #'+str(index_stack.my_stack[-1]+1)+'.'+"'"+str(paren_stack.my_stack[-1])+"'"+'- not closed.\n')

class Node:
    def __init__(self,pera):
        self.pera = pera
        self.next_refer = None
        
class Stack_in_linked_list:
    head = None
    
    def push(self, char):
        if self.head != None:
            new_node = Node(char)
            new_node.next_refer = self.head
            self.head = new_node
            
        else:
            self.head = Node(char)
            
    def pop(self):
        store = self.head
        self.head = self.head.next_refer
        store.next_refer = None
        store.pera = None
        
    def peek(self):
        return self.head.pera
     
def parenthesis_checker_in_linked_list(expression):
    
    paren_stack = Stack_in_linked_list()
    index_stack = Stack_in_linked_list()
    opening = ['(','{','[']
    ending = [')','}',']']
    size = len(expression)
    spinner = 0
    
    while spinner < size:
        if expression[spinner] in opening:
            paren_stack.push(expression[spinner])
            index_stack.push(spinner)
        
        if expression[spinner] in ending:
            
            if paren_stack.head != None:
                see = paren_stack.peek()
                
                if see == '(' and expression[spinner] == ')':
                    paren_stack.pop()
                    index_stack.pop()
                    
                if see == '{' and expression[spinner] == '}':
                    paren_stack.pop()
                    index_stack.pop()
                    
                if see == '[' and expression[spinner] == ']':
                    paren_stack.pop()
                    index_stack.pop()
                    
            elif paren_stack.head == None:

                print(expression)
                print('This expression is NOT correct.')
                print('Error at character #'+str(spinner+1)+'.'+"'"+str(expression[spinner])+"'"+'- not opened.\n')
                return
                  
        spinner = spinner + 1
   
    if paren_stack.head == None:
        print(expression)
        print('This expression is correct.\n')
        
    else:
        print(expression)
        print('This expression is NOT correct.')
        print('Error at character #'+str(index_stack.head.pera + 1)+'.'+"'"+str(paren_stack.head.pera)+"'"+'- not closed.\n')    
               
expression1 = '1+2*(3/4)'
expression2 = '1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14' 
expression3 = '1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14'
expression4 = '1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'

print("\n//===== Parenthesis Balance Checking in an array based stack=====//\n")

parenthesis_checker_in_array(expression1)
parenthesis_checker_in_array(expression2) 
parenthesis_checker_in_array(expression3) 
parenthesis_checker_in_array(expression4)

print("\n//===== Parenthesis Balance Checking in a linked list based stack=====//\n")

parenthesis_checker_in_linked_list(expression1)
parenthesis_checker_in_linked_list(expression2)
parenthesis_checker_in_linked_list(expression3)
parenthesis_checker_in_linked_list(expression4)
