correct_pin = "1234"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    pin = input("Enter your M-pesa pin: ")
    attempts += 1
    
    if pin == "":
        print("you have not entered a pin!")
        continue
    if pin == correct_pin:
        print("pin accepted! transaction completed")
        break
    remaining_attempts = max_attempts - attempts
    if remaining_attempts > 0:
        print(f"wrong pin entered, you have {remaining_attempts} left")
    else:
        print("Account locked!, Too many attempts")
    