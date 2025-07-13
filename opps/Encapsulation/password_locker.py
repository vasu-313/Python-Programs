class Locker:
    def __init__(self, password):
        self.__password = password    # private variable

    def set_password(self, p):
        self.__password = p       # set new password

    def verify_password(self, p):
        if self.__password == p:
            print("password is correct.")
        else:
            print("password is incorrect.")     

# Create locker with initial password
l = Locker("1234")

# Change password
l.set_password("5678")

# Verify with wrong password
l.verify_password("567")  # Output: Password is incorrect         