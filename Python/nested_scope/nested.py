
#this is a nested function example
def calculator(operation):
    def add(a ,b):
        return a + b
    
    def subtract(a ,b):
        return a - b
    
    def multiply(a ,b):
        return a * b
    
    def divide(a ,b):
        return a / b
    
    if operation == "add":
        return add
    
    elif operation == "subtract":
        return subtract
    
    elif operation == "multiply":
        return multiply
    
    elif operation == "divide":
        return divide
    else:
        return"Invalid operation"
    
    
    
result_add = calculator("add")(3,4)
print(f"addition results:{result_add}")
 
 