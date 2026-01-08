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
    return "Valid number"
