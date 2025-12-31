'''A custom exception is a user-defined error type that you create yourself to represent a specific problem in 
your program, instead of using only Python’s built-in exceptions.'''

class NegativeNumberError(Exception):
    pass
class ZeroError(Exception):
    pass
class LargeNumberError(Exception):
    pass

def check_number(num):
    if num < 0:
        raise NegativeNumberError("Negative number not allowed")
    elif num == 0:
        raise ZeroError("Zero is not allowed")
    elif num > 100:
        raise LargeNumberError("Number is too large")
    else:
        print("Valid number")

try:
    n = int(input("Enter the number: "))
    check_number(n)

except NegativeNumberError as e:         #creating the object of exception 
    print("Error:", e)

except ZeroError as e:
    print("Error:", e)

except LargeNumberError as e:
    print("Error:", e)

except ValueError:
    print("Error: Please enter a valid integer")
