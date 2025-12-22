# Create custom exception
class MyError(Exception):
    pass

def check_number(num):
    if num < 0:
        raise MyError("Negative number not allowed")
    print("Valid number")
try:
    n=int(input("Enter the number:"))
    check_number(n)
except MyError as e:
    print("Error:", e)
