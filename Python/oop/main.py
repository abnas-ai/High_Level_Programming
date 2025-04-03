

class User:
    def __init__(self, name, phone, is_admin=False, is_logged_in=False):
        self.name = name
        self.phone = phone
        self.is_admin = is_admin
        self.is_logged_in = is_logged_in
    def user_role(self):
        if self.is_logged_in and self.is_admin:
            return "Dashboard"
        elif not self.is_logged_in:
            return "login page"
        else:
            return "Newsfeed"
        
        
# user1 = User("Ben", "0719181320",  is_logged_in=True, is_admin=False)
# print(f"{user1.name} redirected to {user1.user_role()}")

# user2 = User("Kipngeno", "0719181320", is_logged_in=True, is_admin=False)
# print(f"{user2.name} redirected to {user2.user_role()}")

