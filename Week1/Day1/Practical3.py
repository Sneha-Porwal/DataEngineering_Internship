'''List:
When you check an element in a list, Python looks at each item one by one until it finds the value.
If the list is large, this takes more time.
Method used: Linear search
Time Complexity: O(n)'''

numbers_list = [10, 20, 30, 40, 50]

if 40 in numbers_list:
    print("Element found in list")


#Time Complexity:O(n) (Linear time)

""" Set:
A set uses hashing to find elements directly.
Hashing is a technique where:

A value is passed to a hash function
The function produces a hash value (number)
That hash value is used to decide where the element is stored in memory"""

numbers_set = {10, 20, 30, 40, 50}

if 40 in numbers_set:
    print("Element found in set")


#Time Complexity: O(1) (Constant time, average case)