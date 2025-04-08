


class AbnasFileError(Exception):
    pass

def divide(a, b):
    if b == 0:
        raise AbnasFileError("Division by zero is not allowed")
    return a/b

try:
    f = divide (5, 0)

  
except AbnasFileError as e:
    print(f"Error! cannot divide a number by zero: {e}") 
