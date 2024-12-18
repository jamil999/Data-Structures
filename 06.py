def recursive_selection_sort(array, iter1, iter2):
    arr_length = len(array)
    
    if iter1 < arr_length - 1:
        the_min = iter1
        
        while iter2 < arr_length:
            
            if array[the_min] > array[iter2]:
                the_min = iter2
                
            iter2 += 1
            
        store = array[iter1]
        array[iter1] = array[the_min]
        array[the_min] = store
        
        recursive_selection_sort(array, iter1 + 1, iter1 + 2)

#------------------------------------------------------------

def recursive_insertion_sort(array, iter1):
    arr_length = len(array)
    
    if iter1 < arr_length:
        checker = array[iter1]
        iter2 = iter1 - 1
        
        while iter2 >= 0 and checker < array[iter2]:
            array[iter2 + 1] = array[iter2]
            
            iter2 -= 1
            
        array[iter2 + 1] = checker
        
        recursive_insertion_sort(array, iter1 + 1)
        
#------------------------------------------------------------

class Node1:
    def __init__(self, value):
        self.value = value
        self.next_refer = None
        
class SinglyList:
    
    def __init__(self, a):
        if a == []:
            self.head = None
        else:
            self.head = Node1(a[0])
            main = self.head
            for x in range(1, len(a)):
                next_node = Node1(a[x])
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
                
    def node_location(self, index):
        main = self.head
        for x in range(index):
            main = main.next_refer
        return main

# bubble sort for singly list
    
    def bubble_sort(self):
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
            
# selection sort for singly list
            
    def selection_sort(self):
        main = self.head
        length = 0
        while main != None:
            length = length + 1
            main = main.next_refer
        
        main = self.head
        for x in range(length):
            minimum_index = x
            
            for i in range(x + 1, length):
                if self.node_location(minimum_index).value > self.node_location(i).value:
                    minimum_index = i
                    
            store = self.node_location(minimum_index).value
            self.node_location(minimum_index).value = self.node_location(x).value
            self.node_location(x).value = store
            
               
#---------------------------------------------------------------- 

class Node2:
    def __init__(self, value):
        self.value = value
        self.next_refer = None
        self.previous_refer = None
        
class DoublyList:
    def __init__(self, a):
        self.head = Node2(a[0])
        
        self.last_node = self.head
        for i in range(1,len(a)):
            real_node = Node2(a[i])
            self.last_node.next_refer = real_node
            real_node.previous_refer = self.last_node
            self.last_node = real_node
            
    def showList(self):
        starter = self.head
        while starter != None:
            if starter.next_refer != None:    
                print(starter.value,end='<->')     
            else:
                print(starter.value)
            starter = starter.next_refer
                   
    def node_location(self, index):
        starter = self.head
        for x in range(index):
            starter = starter.next_refer
        return starter
        
    def insertion_sort(self):
        main = self.head
        length = 0
        while main != None:
            length = length + 1
            main = main.next_refer
            
        for x in range(1, length):
            pointer = self.node_location(x).value
            
            next_pointer = x - 1
            
            while pointer < self.node_location(next_pointer).value and next_pointer >= 0:
                self.node_location(next_pointer + 1).value = self.node_location(next_pointer).value
                
                next_pointer = next_pointer - 1
                
            self.node_location(next_pointer + 1).value = pointer

#--------------------------------------------------------------------              
                
def recursion_binary_search(sort_array, left_i, right_i, value):
    if left_i <= right_i:
        middle_i = (left_i + right_i) // 2
        
        if value > sort_array[middle_i]:
            return recursion_binary_search(sort_array, middle_i + 1, right_i, value)
            
        elif value < sort_array[middle_i]:
            return recursion_binary_search(sort_array, left_i, middle_i - 1, value)
            
        else:
            return 'The index of the value: '+str(value)+' is ' +str(middle_i)
    else:    
        return 'The value does not not exist in the array'
    
#--------------------------------------------------------

memory = {}
def fibonacci_of_n(n):
    if n in memory:
        return memory[n]
    
    if n == 0:
        return 0
    
    if  n < 0:
        return 'Can not be determained for negative numbers'
    
    if n <= 2:
        return 1

    else:
        store = fibonacci_of_n(n - 1) + fibonacci_of_n(n - 2)
        
    memory[n] = store
    return store

#------------------------------------------------------------

print("\n//===== Task 1 =====//")

array1 = [13,25,0,-4,7,-1,18,9,-6,21]
recursive_selection_sort(array1, 0, 1) 
print(array1)      
       
print("\n//===== Task 2 =====//")

array2 = [13,25,0,-4,7,-1,18,9,-6,21]
recursive_insertion_sort(array2, 1)
print(array2)    

print("\n//===== Task 3 =====//")

array3 = [60, 20, 40, 80, 10, 30]
singly_list1 = SinglyList(array3)
print("\n--Before bubble sort--")
singly_list1.showList()
singly_list1.bubble_sort()
print("\n--After bubble sort--")
singly_list1.showList() 

print("\n//===== Task 4 =====//")

array4 = [60, 20, 40, 80, 10, 30]
singly_list2 = SinglyList(array4)
print("\n--Before selection sort--")
singly_list2.showList()
singly_list2.selection_sort()
print("\n--After selection sort--")
singly_list2.showList()

print("\n//===== Task 5 =====//")

array5 = [60, 20, 40, 80, 10, 30]
doubly_list1 = DoublyList(array5)
print("\n--Before insertion sort--")
doubly_list1.showList()
print("\n--After insertion sort--")
doubly_list1.insertion_sort()
doubly_list1.showList()

print("\n//===== Task 6 =====//")

sorted_array = [1,5,6,7,8,9,12,15,17]
print(recursion_binary_search(sorted_array, 0, len(sorted_array) - 1, 15))

print("\n//===== Task 7 =====//")

print(fibonacci_of_n(100))
