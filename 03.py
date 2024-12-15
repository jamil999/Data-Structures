class Node:
    def __init__(self, value):
        self.value = value
        self.next_refer = None
        self.previous_refer = None
        
class DoublyList:
    def __init__(self, a):
        self.head = Node(None)
        self.head.next_refer = self.head
        self.head.previous_refer = self.head
        
        starter = self.head
        for i in range(len(a)):
            real_node = Node(a[i])
            real_node.next_refer = starter.next_refer
            real_node.previous_refer = starter
            starter.next_refer = real_node
            real_node.next_refer.previous_refer = real_node
            starter = starter.next_refer
    
    def showList(self):
        
        if self.head.next_refer == self.head:
            print('Empty List')
            
        else:    
            starter = self.head.next_refer
            while starter != self.head:
                if starter.next_refer != self.head:    
                    print(starter.value,end='<->')     
                else:
                    print(starter.value)
                starter = starter.next_refer
            
    def insert(self, newElement, index = None):
        starter = self.head.next_refer
        while starter != self.head:
            if starter.value == newElement:    
                print('The element already exists so can not be inserted')
                return
            starter = starter.next_refer
            
        if index != None:
            insert_in = Node(newElement)
            size = 0
            starter = self.head.next_refer
            while starter != self.head:
                size += 1
                starter = starter.next_refer
        
            if index > size or index < 0:
                    print('Invalid Index')
                    return
                
            if index == 0:
                insert_in.next_refer = self.head.next_refer
                insert_in.previous_refer = self.head
                self.head.next_refer.previous_refer = insert_in
                self.head.next_refer = insert_in
                
            else:
                
                starter = self.head.next_refer
                before_index = 0

                while before_index != index - 1:
                    before_index += 1
                    starter = starter.next_refer
                   
                insert_in.next_refer = starter.next_refer
                insert_in.previous_refer = starter
                starter.next_refer.previous_refer = insert_in
                starter.next_refer = insert_in       
                
        else:
            insert_end = Node(newElement)
            insert_end.next_refer = self.head
            insert_end.previous_refer = self.head.previous_refer 
            self.head.previous_refer.next_refer = insert_end
            self.head.previous_refer = insert_end       
        
    def remove(self, index):
        size = 0
        starter = self.head.next_refer
        while starter != self.head:
            size += 1
            starter = starter.next_refer
        
        if index > size-1 or index < 0:
            print('Invalid Index')
            return
        
        starter = self.head.next_refer
        go_to = 0
        while go_to != index:
            go_to += 1
            starter = starter.next_refer
            
        starter.next_refer.previous_refer = starter.previous_refer
        starter.previous_refer.next_refer = starter.next_refer
            
    def removeKey(self, deletekey):
        starter = self.head.next_refer
        while starter != self.head:
            if starter.value == deletekey:
                starter.next_refer.previous_refer = starter.previous_refer
                starter.previous_refer.next_refer = starter.next_refer
                return
            starter = starter.next_refer
            
        print('The key does not exist')        
        
#================Tester Code===============#

print("\n//=====Task 2.1, 2.2 -- Constructor & showList=====//")

arr1 = [1,2,3,4,5]
dll = DoublyList(arr1)
dll.showList()

arr1 = []
dll = DoublyList(arr1)
dll.showList()

print("\n//=======Task 2.3, 2.4 -- Insert=======//")  

arr1 = [1,2,3,5,6]
arr1 = DoublyList(arr1)
arr1.showList() 
arr1.insert(7)
arr1.showList()
arr1.insert(3)
arr1.showList()  
arr1.insert(0, 0)
arr1.showList() 
arr1.insert(4, 4)
arr1.showList() 
arr1.insert(8, 8)
arr1.showList() 
arr1.insert(2)
arr1.insert(5, 4)       

print("\n//=======Task 2.5 -- remove=======//")

arr1.showList()
arr1.remove(0)
arr1.showList() 
arr1.remove(7) 
arr1.showList() 
arr1.remove(7)
arr1.showList()
arr1.remove(3)
arr1.showList()  
arr1.remove(13)
arr1.showList()

print("\n//=======Task 2.6 -- removeKey=======//")

arr1.showList()
arr1.removeKey(1)
arr1.showList() 
arr1.removeKey(7) 
arr1.showList() 
arr1.removeKey(5)
arr1.showList()
arr1.removeKey(4) 
arr1.showList()
