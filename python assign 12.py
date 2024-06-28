
### 1. Write a Python program to Extract Unique values dictionary values?"
'''
def extract_unique_values(d):
    unique_values = set()
    
    # Iterate through the values of the dictionary
    for value in d.values():
        unique_values.add(value)
    
    return unique_values

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2}
unique_values = extract_unique_values(my_dict)
print("Unique values:", unique_values)
'''
 ### 2. Write a Python program to find the sum of all items in a dictionary?"
'''
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2}
sum=0
for values in my_dict.values():
   sum=sum+values
print(sum)   
'''
##3. Write a Python program to Merging two Dictionaries?"
'''def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

# Example usage:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = merge_dicts(dict1, dict2)
print("Merged dictionary:", merged_dict)
'''
### 4. Write a Python program to convert key-values list to flat dictionary?
'''
def list_to_flat_dict(key_value_list):
    flat_dict = {}
    for pair in key_value_list:
        key, value = pair
        flat_dict[key] = value
    return flat_dict

# Example usage:
key_value_list = [('a', 1), ('b', 2), ('c', 3)]
flat_dict = list_to_flat_dict(key_value_list)
print("Flat dictionary:", flat_dict)
'''
### 5. Write a Python program to insertion at the beginning in OrderedDict?"

'''
from collections import OrderedDict

def insert_at_beginning(ordered_dict, key, value):
    # Move the specified key to the beginning of the OrderedDict
    ordered_dict[key] = value
    ordered_dict.move_to_end(key, last=False)


ordered_dict = OrderedDict([('b', 2), ('c', 3)])
print("Original OrderedDict:", ordered_dict)

# Inserting 'a' at the beginning
insert_at_beginning(ordered_dict, 'a', 1)
print("OrderedDict after insertion at the beginning:", ordered_dict)


'''
 ### 6. Write a Python program to check order of character in string using OrderedDict()?"


'''
from collections import OrderedDict

def check_order_of_characters(input_string, pattern):
    # Create an OrderedDict to store the occurrence of characters in the input string
    char_occurrence = OrderedDict.fromkeys(input_string, 0)

    # Iterate through the input string to count the occurrences of characters
    for char in input_string:
        char_occurrence[char] += 1

    # Initialize a variable to keep track of the index of the pattern character
    pattern_index = 0

    # Iterate through the characters in the ordered dictionary
    for char in char_occurrence:
        # If the character matches the current character in the pattern, move to the next character in the pattern
        if char == pattern[pattern_index]:
            pattern_index += 1
            # If all characters in the pattern have been found, return True
            if pattern_index == len(pattern):
                return True

    # If the entire pattern has not been found, return False
    return False

input_string = "hello world"
pattern = "lo"
result = check_order_of_characters(input_string, pattern)
print(f"Pattern '{pattern}' {'is' if result else 'is not'} in order in the string '{input_string}'.")
'''

"### 7. Write a Python program to sort Python Dictionaries by Key or Value?"
my_dict = {'a': 1, 'd': 2, 'c': 3, 'b': 2}
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)

