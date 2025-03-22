# counter = 0
# while counter <= 5:
#     counter += 1
#     print(counter)
    
    
# username = input("Enter your username: ")
# list_of_banned_users = ["rop", "admin", "root", "kirui", "Ben"]
# while username:
#     if username in list_of_banned_users:
#         print("You have been banned by admin")
    
#         print("try another username")
#     username = input("Enter your username: ").lower()
#     print("You have been successfully logged in")



#password = "secret"
# user_input = ""

# while user_input != password:
#     user_input = input("Enter the password: ")

# print("Access granted!")

        
# username = input("Enter your username: ")
# while username != "Q".lower():
#     print(f"your username is {username})")
#     username = input("Enter your username: ").lower()
    
    
# x = 1

# while x < 1:
#   print("x" * 20)

# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#       print(f"{i} x {j} = {i*j}")
#       j += 1
#     print("__________")
#     i += 1


# i = 1
# while i <= 5:
#     print("*" * i)
#     i = i + 1
# print("Done")


secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess =  int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("You failed terribly!")