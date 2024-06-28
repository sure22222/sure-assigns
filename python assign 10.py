### 1. Write a Python program to find sum of elements in list?"

from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum)

##2. Write a Python program to  Multiply all numbers in the list?
from functools import reduce
numbers = [1, 2, 3, 4, 5]
Product= reduce(lambda x, y: x * y, numbers)
print("Sum of numbers:",Product)

### 3. Write a Python program to find smallest number in a list?
 
numbers = [1, 2, 3, 4, 5]
print("Smallest number is:",min(numbers))

### 4. Write a Python program to find largest number in a list?
numbers = [1, 2, 3, 4, 5]
print("Largest number is:",max(numbers))


### 5. Write a Python program to find second largest number in a list?"
list=[3,8,9,6,4,99]
list2=sorted(list)
print("The second largest number is:",list2[len(list2)-2])

### 6. Write a Python program to find N largest elements from a list?"

import heapq

def find_N_largest_elements(lst, N):
    return heapq.nlargest(N, lst)

my_list = [10, 4, 7, 1, 9, 3, 15, 6]
N = 3  # Number of largest elements to find
largest_elements = find_N_largest_elements(my_list, N)
print(f"The {N} largest elements in the list are:", largest_elements)

### 7. Write a Python program to print even numbers in a list?"
print([e for e in range(1,11) if e%2==0 ])

### 8. Write a Python program to print odd numbers in a List?
print([e for e in range(1,11) if e%2!=0 ])

### 9. Write a Python program to Remove empty List from List?"

my_list = [10, 4, 7, 1, 9, 3, 15, 6,[]]
my_list.remove([])
print(my_list)


### 10. Write a Python program to Cloning or Copying a list?"
list=[1,2,4,8]
list2=list.copy()
print(list2)

 ### 11. Write a Python program to Count occurrences of an element in a list?"


list=[1,2,4,8,4,2]
for e in set(list):
   print('Frequency of element',e,':',list.count(e))
