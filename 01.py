#method 1 
def shiftLeft(source,k):
    first = 0
    last = k
    length = len(source)
    
    while length > last:
        source[first] = source[last]
        source[last] = 0
        first+=1
        last+=1
        
    print(source)

source=[10,20,30,40,50,60]
shiftLeft(source,3)

#method 2
def rotateLeft(source,k):
    first = 0
    last = k
    length = len(source)
    
    while length > last:
        extra = source[first]
        source[first] = source[last]
        source[last] = extra
        first+=1
        last+=1
        
    print(source)

source=[10,20,30,40,50,60]
rotateLeft(source,3)

#method 3
def remove(source, size, idx):
    
    if(idx<0 or idx>size):
        print("Invalid index!")
        
    else:
        first = idx
        last = size
    
        while first+1 < last:
            source[first] = source[first+1]
            source[first+1]=0
            first+=1
        
        print(source)
 
source=[10,20,30,40,50,0,0]
remove(source,5,2)

#method 4
def removeAll(source, size, element):
    first = 0

    while first < size:
        if source[first] == element :
            similar = first
            
            while similar+1 < size:
                source[similar] = source[similar+1]
                source[similar+1] = 0
                similar+=1
                
        if source[first] == element:
            first -=1
 
        first+=1

    print(source)
    
source=[10,2,30,2,50,2,2,0,0]
removeAll(source,7,2)

#method 5
def splitting(array):
    first = 0
    sum1 = 0
    sum2= 0
    while first < len(array):
        
        for x in range(0, first+1):
            sum1 = sum1 + array[x]
            
        for j in range(first+1, len(array)):
            sum2 = sum2 + array[j]
            
        if sum1 == sum2:
            return True

        first+=1
        sum1=0
        sum2=0
        
    return False

array = [2, 1, 1, 2, 1]
print(splitting(array))

#method 6
def series(n):
    series_array=[0]*(n*n)
    extra = n
    
    for i in range(1, n + 1):
        last= (n*n)- i
        
        for x in range(1, extra + 1):
            series_array[last] = i
            last -= n
            
        extra -= 1
    print(series_array)
        
n = int(input('Insert the value of the n for the array series:'))
series(n)

#method 7
def maxCount(source):
    increaser = 1
    highest = 0
    
    for x in range(len(source)-1):
        if source[x] == source[x + 1]:
            increaser += 1
      
            
            if increaser > highest:
                highest = increaser
             
        else:
            increaser = 1
                
    print(highest)       
        
source =   [1,1,2, 2, 1, 1,1,1]
maxCount(source)

#method 8
def repetition(source):
    size = len(source)
      
    for i in range(size):
        increaser = 1
        if source[i]!= None:
            
            for x in range(i+1, size):
                if source[i] == source[x]:
                    increaser += 1
                    source[x] = None
         
            source[i] = increaser
               
    increaser = 0 
    for y in range(size):
        if source[y]!=None and source[y]!=1:
            for z in range(y + 1, size):
                if source[y] == source[z]:
                    increaser +=1    

    if increaser >= 1:
        return True
    else:

        return False            
          
source = [4,5,6,6,4,3,6,4]
print(repetition(source))

#method 9
def palindrome(source, start, size):
    f_point = start
    l_point = (start + size - 1)%len(source)
  
    counter = 0
    while counter <= size//2:

        if source[f_point] != source[l_point]:
            return False

        f_point = (f_point + 1)%len(source)
        l_point -= 1
        if l_point < 0:
            l_point = len(source) - 1
            
        counter += 1
    return True
source =  [10,20,0,0,0,10,20,30]
print(palindrome(source, 5, 5))

#method 10
def intersection(cir_array_1, start_1, size_1, cir_array_2, start_2, size_2):
    new_array = []
    i1 = start_1 
    
    for i in range(size_1):
        i2 = start_2
        
        for x in range(size_2):
            if cir_array_1[i1] == cir_array_2[i2] and cir_array_1[i1] not in new_array:
                new_array = new_array +[cir_array_1[i1]]
                
            i2 = (i2 + 1) % len(cir_array_2)
                
        i1 = (i1 + 1) % len(cir_array_1)
        
    print(new_array)
      
cir_array_1 = [40,50,0,0,0,10,20,30]
cir_array_2 =  [10,20,5,0,0,0,0,0,5,40,15,25]
intersection(cir_array_1, 5, 5, cir_array_2, 8, 7)

#method 11
def musicChairGame(array):
    length = 7
    
    while length != 1:
        import random
        randm = random.randint(0, 3)
        
        if randm == 1:
            eli_index = length // 2
 
            while eli_index+1 < length:
                array[eli_index] = array[eli_index+1]
                eli_index += 1
            array[length - 1]=0    
            length -= 1
        
        else:
            swap = array[length-1]
            end = length-1
            while end>=1:
                array[end]=array[end-1]
                end -= 1
                
            array[0] = swap

    print("Music Chair Game's Winner':",array[0])
                  
array = ['Abul', 'Basir', 'Rahat', 'Mehedi', 'Robi', 'Jakir', 'Jamil']
musicChairGame(array)
