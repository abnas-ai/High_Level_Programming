
me = "Ben"

def my_my_name():
    me = "Ronoh"
    print(me)
    
my_my_name


count = 1  # Global variable

def increment():
    global count  # Modify global variable
    count = 2
    print(count)

increment()  # Output: 1

