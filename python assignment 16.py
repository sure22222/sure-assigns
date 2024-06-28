### 1. Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?. Examples stutter('incredible') ➞ 'in... in... incredible?' stutter('enthusiastic') ➞ 'en... en... enthusiastic?' stutter('outstanding') ➞ 'ou... ou... outstanding?'


### Hint :- Assume all input is in lower case and at least two characters long.
'''def slicing(word):
    for i in range(0,2):
      new_word= print(word[0:2]+'...',end=' ')
    return new_word 
word=input('Enter the word')
slicing(word)
'''
##2.Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place
'''import math 
radians = 1.5708
degrees = math.degrees(radians)
print("The degree of the given radian is :",round(degrees,1))
'''

### 3. In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number. Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.
'''
def is_curzon_number(num):
    numerator = 2**num + 1
    denominator = 2*num + 1
    return numerator % denominator == 0
num=int(input('Enter any number:'))
# Test the function
print(is_curzon_number(num)) '''


### 4. Given the side length x find the area of a hexagon.
x=int(input('Enter any value:'))
print((3*3**0.5*x**2)/2)

###5.  Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.
def decimal_to_binary(decimal_number):
    binary_representation = bin(decimal_number)[2:]
    return binary_representation

# Test the function
print(decimal_to_binary(10))


