import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
def generate_password_operations():
    length = int(input("Enter the length of the password: "))
    password = generate_random_password(length)
    print(f"Generated Password: {password}")
generate_password_operations()
