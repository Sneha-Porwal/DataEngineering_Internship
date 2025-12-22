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
A set uses hashing to find elements directly."""

numbers_set = {10, 20, 30, 40, 50}

if 40 in numbers_set:
    print("Element found in set")


#Time Complexity: O(1) (Constant time, average case)