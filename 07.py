class KeyIndex:
    def __init__(self,a):
        self.k = []
        maximum = 0
        self.minimum = 0
        for i in range(len(a)):
            if a[i] > maximum:
                maximum = a[i]
                
            if a[i] < 0:
                if a[i] < self.minimum:
                     self.minimum = a[i]
        
        if self.minimum == 0:
            self.k = [0]*(maximum + 1)
            for x in a:
                self.k[x] = self.k[x] + 1
                
        else:
            self.k = [0] * ((self.minimum * -1) + (maximum + 1))
            for x in a:
                self.k[x + (self.minimum * -1)] = self.k[x + (self.minimum * -1)] + 1
        
        
    def search(self, value):
        
        if self.minimum == 0:
            if value >= len(self.k) or value < 0:
                return False
            if self.k[value] >= 1:
                return True
            else:
                return False
            
        else:
            if (value + (self.minimum * -1)) >= len(self.k) or value < self.minimum:
                return False
            if self.k[value + (self.minimum * -1)] >= 1:
                return True
            else:
                return False
        
    def sort(self):
        sorted_array = []
        for i in range(len(self.k)):
            count = 0
            while count < self.k[i]:
                sorted_array = sorted_array + [i + self.minimum]
                count = count + 1
                
        return sorted_array
            
class hashtable_creator:
    def __init__(self,a):
        self.given_array = a
        self.my_hashtable = [0] * 9
        
    def hashing(self):
        if len(self.given_array) > 9:
            return 'the String array contains more than 9 values. Can not create Hashtable.'
        
        for s in self.given_array:
            count_constant = 0
            digits_sum = 0
            for i in s:
                if not ord(i) >= 65 and ord(i) <= 90:
                    digits_sum = digits_sum + int(i)
                else:
                    if i not in 'AEIOU':   
                        count_constant = count_constant  + 1
                        
            new_index = ((count_constant*24)+digits_sum)%9
            
            if self.my_hashtable[new_index] == 0:
                self.my_hashtable[new_index] = s
                
            else:
                next_new_index = (new_index + 1) % 9
                while self.my_hashtable[next_new_index] != 0:
                    next_new_index = (next_new_index + 1) % 9
                self.my_hashtable[next_new_index] = s
                
        return self.my_hashtable


print('\n =============== Tester Statements ================ ')              
print('\n        ============= Task 1 =============     ')
print('\n           ======== Example 1 =========      ')
 
array1 = [5,4,7,6,2,3,1,8,0]
print('An array of integers:') 
print(array1)     
p1 = KeyIndex(array1)
find1 = 2
print('Need to find the value:',find1)         
print(p1.search(find1))
print('Sorted array:')
print(p1.sort())

print('\n           ======== Example 2 ==========      ')

array2 = [3,2,6,5,7,2,3,7,8,1]
print('An array of integers:') 
print(array2)     
p2 = KeyIndex(array2)
find2 = 2
print('Need to find the value:',find2)         
print(p2.search(find2))
print('Sorted array:')
print(p2.sort())

print('\n           ======== Example 3 ==========      ')

array3 = [-5,4,-7,6,2,3,-4,1,8,-5,0,-3] 
print('An array of integers:') 
print(array3)     
p3 = KeyIndex(array3)
find3 = -7
print('Need to find the value:',find3)         
print(p3.search(find3))
print('Sorted array:')
print(p3.sort())

print('\n        ============= Task 2 =============     ')
print('\n           ======== Example 1 =========      ')

array4 = ['ST1E89B8A32'] 
print('An array of Strings:')
print(array4) 
p4 = hashtable_creator(array4)
print('The Hashtable:')
print(p4.hashing())

print('\n           ======== Example 2 =========      ')

array5 = ['ST1E89B8A32','ST1E89B8A32','ST1E89B8A32','ST1E89B8A32','ST1E89B8A32','ST1E89B8A32'] 
print('An array of Strings:')
print(array5) 
p5 = hashtable_creator(array5)
print('The Hashtable:')
print(p5.hashing())

print('\n           ======== Example 3 =========      ')

array6 = ['JAMIL2R9','RAF4HKI3','AS1GT5E','3RGTHU6','SERT42HY','KITRQ341H','RRE12U','TRT5','RHRS3AW'] 
print('An array of Strings:')
print(array6) 
p6 = hashtable_creator(array6)
print('The Hashtable:')
print(p6.hashing())


print('\n           ======== Example 4 =========      ')

array7 = ['JA9','RI3','AS1E','3H6','SEFHY','Q341H','R12U','TRT5','R3AW','FAE1'] 
print('An array of Strings:')
print(array7) 
p7 = hashtable_creator(array7)
print('The Hashtable:')
print(p7.hashing())
