### 1. Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
class DivisibleBySevenGenerator:
    def __init__(self, n):
        self.n = n

    def generate_divisible_by_seven(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i


n = int(input('Enter the number:'))
generator = DivisibleBySevenGenerator(n)
for num in generator.generate_divisible_by_seven():
    print(num)


### 2. Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

def word_frequency(input_text):
    words = input_text.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def sorted_word_frequency(input_text):
    frequency = word_frequency(input_text)
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[0])
    return sorted_frequency

if __name__ == "__main__":
    input_text = input("Enter the text: ")
    sorted_frequency = sorted_word_frequency(input_text)
    for word, freq in sorted_frequency:
        print(f"{word}: {freq}")

### 3. Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
class Person:
    def getGender(self):
        raise NotImplementedError("Subclasses must implement getGender method")

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")


male_person = Male()
female_person = Female()

male_person.getGender()  # Output: Male
female_person.getGender()  # Output: Female
        



##4.### 4. Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ['Play', "Love"] and the object is in ["Hockey","Football"].
import random
l1= ["I", "You"]
l2= ['Play', "Love"]
l3= ["Hockey","Football"]
n=0
while n<9:
 print(random.choice(l1)+random.choice(l2)+random.choice(l3))
 n+=1 

'
### 5. Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!"
import zlib

def compress_string(s):
    # Convert string to bytes
    s_bytes = s.encode('utf-8')
    # Compress the bytes
    compressed_data = zlib.compress(s_bytes)
    return compressed_data

def decompress_string(compressed_data):
    # Decompress the bytes
    decompressed_data = zlib.decompress(compressed_data)
    # Convert decompressed bytes to a string
    decompressed_string = decompressed_data.decode('utf-8')
    return decompressed_string

# Original string
original_string = "hello world!hello world!hello world!hello world!"

# Compress the string
compressed_data = compress_string(original_string)
print("Compressed data:", compressed_data)

# Decompress the compressed data
decompressed_string = decompress_string(compressed_data)
print("Decompressed string:", decompressed_string)

"### 6. Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list."
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element not found

# Test the function
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11
index = binary_search(sorted_list, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the list.")
