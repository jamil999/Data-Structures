def factorial_of_n(n):
    
    if n == 0 or n == 1:
        return 1
    
    if n < 0:
        return 'Can not be determained for negative numbers'
    
    else:
        return n * factorial_of_n(n - 1)
    
#---------------------------------------------------    
    
def fibonacci_of_n(n):
    if n == 0:
        return 0
    
    if  n < 0:
        return 'Can not be determained for negative numbers'
    
    if n <= 2:
        return 1

    else:
        return fibonacci_of_n(n - 1) + fibonacci_of_n(n - 2)
   
#---------------------------------------------------
    
def array_elements(array, index):
    if index == len(array):
        return
    
    else:
        print(array[index])
        return array_elements(array, index + 1)
    
#---------------------------------------------------

def powerN(base, n):
    if n == 0:
        return 1
    
    else:
        return base * powerN(base, n - 1)
    
#---------------------------------------------------

def decimal_to_binary(n):  
    if n == 0:
        return 0
    
    else:
        return decimal_to_binary(n // 2)*10 + (n % 2)

#---------------------------------------------------

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
                
def linked_list_addelements(main):
    
    if main.next_refer == None:
        return main.value
    
    else:
        return main.value + linked_list_addelements(main.next_refer)

#---------------------------------------------------

def linked_list_showreverse(main):
    if main == None:
        return
    
    else:
        linked_list_showreverse(main.next_refer)
        print(main.value)  
        
#---------------------------------------------------        

def hocBuilder(height):
    if height == 1:
        return 8

    else:
        return 5 + hocBuilder(height - 1)
       
#---------------------------------------------------

def show_normal_stair(n):
    if n == 0:
        return

    show_normal_stair(n - 1)
    stair_numbers(n)
    print()

def stair_numbers(n):

    if n == 1:
        print(n, end=' ')
        return

    stair_numbers(n - 1)
    print(n, end=' ')
    
#---------------------------------------------------
    
def show_mirrored_stair(n,s):
    if n < s:
        return
    
    stair_space(n - s)
    stair_mirrored_numbers(s)
    print()
    show_mirrored_stair(n, s + 1)
      
def stair_space(n):
    if n == 0:
        return 
    
    print(' ', end=' ')
    stair_space(n - 1)

def stair_mirrored_numbers(n):
    if n == 1:
        print(n, end=' ')
        return

    stair_mirrored_numbers(n - 1)
    print(n, end=' ')

#---------------------------------------------------

class FinalQ:
    def print(self, array, idx):
        if(idx < len(array)): 
            profit = self.calcProfit(array[idx])
            print('Investment: '+str(array[idx])+'; '+'Profit: '+str(profit))
  
    def calcProfit(self, investment):
        if investment <= 25000:
            return 0.0
    
        if investment <= 100000:
            return 4.5 + self.calcProfit(investment - 100)
    
        else:
            return 80 + self.calcProfit(investment - 1000)
        
#---------------------------------------------------

print("\n//===== Task 1(a) =====//")

print(factorial_of_n(6))

print("\n//===== Task 1(b) =====//")

print(fibonacci_of_n(6))    

print("\n//===== Task 1(c) =====//")

array1 = [10, 20, 30, 40]
array_elements(array1, 0)

print("\n//===== Task 1(d) =====//")

print(powerN(3, 1))
print(powerN(3, 2))
print(powerN(3, 3))

print("\n//===== Task 2(a) =====//")

print(decimal_to_binary(10))

print("\n//===== Task 2(b) =====//")

linked_list = MyList(array1)
print(linked_list_addelements(linked_list.head))

print("\n//===== Task 2(c) =====//")

linked_list_showreverse(linked_list.head)

print("\n//===== Task 3 =====//")

print(hocBuilder(3))

print("\n//===== Task 4(a) =====//")

show_normal_stair(5)

print("\n//===== Task 4(b) =====//")

show_mirrored_stair(5, 1)

print("\n//===== Task 5 =====//")

array=[25000,100000,250000,350000] 
f = FinalQ() 
f.print(array,3)
