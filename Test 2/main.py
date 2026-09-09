def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the division result of a by b, handling division by zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b