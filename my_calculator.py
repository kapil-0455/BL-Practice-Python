
def add(num1 , num2):
    """Function add two number"""
    return num1 + num2

def subtract(num1 , num2):
    """Function subtract two number"""
    return num1 - num2

def multiply(num1 , num2):
    """Function mutiply two number"""
    return num1 * num2

def divide(num1 , num2):
    """Function divide two number"""
    if(num2 == 0):
        raise ValueError("Cannot divide by zero")
    return num1 / num2
