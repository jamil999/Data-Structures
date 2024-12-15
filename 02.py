class Node:
    def __init__(self, value):
        self.value = value
        self.next_refer = None
        
class MyList:
    def __init__(self, a):
        if a == []:
            self.head = None
        else:
            self.head = Node(a[0])
            main = self.head
            for x in range(1, len(a)):
                next_node = Node(a[x])
                main.next_refer = next_node
                main = main.next_refer
            
    def showList(self):
        if self.head != None:
            main = self.head
            while main != None:
                if main.next_refer != None:
                    print(main.value,end='->')
                else:
                    print(main.value)
                main = main.next_refer
                
        else:
            print('Empty list')

    def isEmpty(self):
        
        if self.head == None:
            return True
        else:
            return False
        
    def clear(self):
        
        self.head = None
        
    def insert(self, newElement, index = None):
        if index == None:
     
            latest_node = Node(newElement)
      
            if self.head == None:
                self.head = latest_node
            
            main = self.head
            while main != None:
                
                if main.value == latest_node.value:
                    print('Key', latest_node.value, 'already exists.')
                    return
        
                main = main.next_refer
      
            main = self.head
            while main.next_refer is not None:
                main = main.next_refer
            main.next_refer = latest_node
            
        else:
            insert_node = Node(newElement)
            length = 0
            main = self.head
            while main != None:
                if main.value == insert_node.value:
                    print('As the key already exists the new key can not be inserted')
                    return
                length += 1
                main = main.next_refer
                
            if index < 0 or index > length:
                print('Invalid Index.')
                return
            
            if index == 0:
                insert_node.next_refer = self.head
                self.head = insert_node
                
            else:
                main = self.head
                stopper = 0
                while stopper is not (index - 1):
            
                    main = main.next_refer
                    stopper = stopper + 1
                    
                keep = main.next_refer  
                main.next_refer = insert_node
                insert_node.next_refer = keep
                     
    def remove(self, deletekey):
        main = self.head
        
        if main.value == deletekey:
            self.head = main.next_refer
            return
        
        previous = None
        while main != None:
    
            if main.value == deletekey:
                
                previous.next_refer = previous.next_refer.next_refer
                return None
   
            previous = main
            main = main.next_refer
            
        print('key',deletekey,'does not exist')  
        
    def evenList(self):
        main = self.head
        main2 = None
        end2 = None
        
        while main != None:
            if main.value % 2 ==0:
                even_node = Node(main.value)
                if main2 == None:
                    main2 = even_node
                    end2 = even_node
                else:
                    end2.next_refer = even_node
                    end2 = even_node
                    
  
            main = main.next_refer
            
        self.head = main2
        return 

    def find(self, element):
        main = self.head
        while main != None:
            if main.value  == element:
                return True
                 
            main = main.next_refer    
            
        return False

    def reverseList(self):
        main = self.head
        main2 = None
        
        while main != None:
            
            reverse_node = main.next_refer
            main.next_refer = main2
            main2 = main 
            
            main = reverse_node
            
        self.head = main2
        
    def sort(self):
        counter = 0
        main = self.head
        while main != None:
            counter += 1
            main = main.next_refer
        
        main = self.head
        for x in range(counter):
            after = main.next_refer
            
            for i in range(counter - x - 1):
                
                if main.value > after.value:
                    saver = main.value
                    main.value = after.value
                    after.value = saver
                    
                after = after.next_refer
                    
            main = main.next_refer
            
    def sum(self):
        total = 0
        main = self.head
        while main != None:
            
            total = total + main.value
            main = main.next_refer
            
        return total
        
    def rotateKTimes(self, k, direction):
        
        if direction == 'left':
            for i in range(k):
                main = self.head
                
                new_main = main.next_refer
                last = main
                
                while last.next_refer != None:
                    last = last.next_refer
                    
                last.next_refer = main
                main.next_refer = None
                
                self.head = new_main
        
        if direction == 'right':
            for x in range(k):
                
                main = self.head
                previous = None
                while main.next_refer != None:
          
                    previous = main
                    main = main.next_refer
                    
                saved_last = previous.next_refer
                previous.next_refer = None
                saved_first = self.head
                self.head = saved_last
                saved_last.next_refer = saved_first

#==========================Tester Code==========================#
        
#Task-2.1, 2.2 -- Constructor & showList
print("\n//=======Task 2.1, 2.2 -- Constructor & showList=======//")
a = [10, 20, 30, 40, 50, 60]
l1 = MyList(a)
l1.showList() 

#Task-2.3 -- isEmpty
print("\n//========Task 2.3 -- isEmpty========//")
isListEmpty = l1.isEmpty()
print(isListEmpty) 

b = []
l2 = MyList(b)
isListEmpty = l2.isEmpty()
print(isListEmpty) 

#Task-2.4 -- Clear
print("\n//=======Task 2.4 -- Clear =======//")
print("Before clearing Linked List")
l1.showList() 
l1.clear()

print("After clearing Linked List")
l1.showList()

#Task-2.5, 2.6 -- Insert
print("\n//=======Task 2.5, 2.6 -- Insert=======//")
c = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l3 = MyList(c)
l3.showList() 
l3.insert(100)
l3.showList() 
l3.insert(0, 0)
l3.showList() 
l3.insert(110, 5)
l3.showList() 
l3.insert(120, 12)
l3.showList() 
l3.insert(50) 

#Task-2.7 -- Remove
print("\n//=======Task 2.7 -- Remove=======//")
l3.showList()
l3.remove(0)
l3.showList() 
l3.remove(110) 
l3.showList() 
l3.remove(120)
l3.showList() 
l3.remove(120)

#Task-2.8 -- EvenList
print("\n//=======Task 2.8 -- EvenList =======//")
d = [1, 2, 5, 3, 8]
f = [101, 120, 25, 91, 87, 1]
l4 = MyList(d)
l4.evenList()
l4.showList()
l8 = MyList(f)
l8.evenList()
l8.showList()

#Task-2.9 -- Find
print("\n//=======Task 2.9 -- Find =======//")
l1 = MyList(d)
found = l1.find(7)
print(found)
l7 = MyList(f)
found = l7.find(87)
print(found)

#Task-2.10 -- Reverse List
print("\n//=======Task 2.10 -- Reverse =======//")
print("Before Reverse: ", end='')
l1.showList()
l1.reverseList()
print("After Reverse: ", end='')
l1.showList()

#Task-2.11 -- Sort
print("\n//=======Task 2.11 -- Sort =======//")
l2 = MyList(d)
print("Before Sort: ", end='')
l2.showList()
l2.sort()
print("After Sort: ", end='')
l2.showList()

#Task-2.12 -- Sum of Elements
print("\n//=======Task 2.12 -- Sum of Elements =======//")
l3 = MyList(d)
l3.showList()
total = l3.sum()
print("Sum of Elements:", total)

#Task-2.13 -- Rotate
print("\n//=======Task 2.13 -- Rotate =======//")
a = [3, 2, 5, 1, 8]
l5 = MyList(a)
l5.showList()
l5.rotateKTimes(2, "left")
l5.showList()
l6 = MyList(a)
l6.rotateKTimes(2, "right")
l6.showList()
