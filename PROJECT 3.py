password="D120"
user_password=input("Enter your password:")
while user_password!=password:
    print("Incorrect password")
    user_password = input("Enter your password:")
print("Access granted")
