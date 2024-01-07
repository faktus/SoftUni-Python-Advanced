def is_valid_password(password):
    # Check if the password meets all the rules
    if len(password) < 8:
        print("Password must be at least 8 characters long!")
    if not all(char.isalnum() or char == "_" for char in password):
        print("Password must consist only of letters, digits and _!")
    if not any(char.isupper() for char in password):
        print("Password must consist at least one uppercase letter!")
    if not any(char.islower() for char in password):
        print("Password must consist at least one lowercase letter!")
    if not any(char.isdigit() for char in password):
        print("Password must consist at least one digit!")
    

def make_uppercase(password, index):
    if 0 <= index < len(password):
        password = password[:index] + password[index].upper() + password[index + 1:]
        print(password)
    return password

def make_lowercase(password, index):
    if 0 <= index < len(password):
        password = password[:index] + password[index].lower() + password[index + 1:]
        print(password)
    return password

def insert_character(password, index, char):
    if 0 <= index <= len(password):
        password = password[:index] + char + password[index:]
        print(password)
    return password

def replace_character(password, char, value):
    if char in password:
        new_char = chr(ord(char) + value)
        password = password.replace(char, new_char)
        print(password)
    return password

password = input()

while True:
    command = input().split()
    action = command[0]

    if action == "Complete":
        break

    if action == "Make":
        cmd = command[0]
        case = command[1]
        index = int(command[2])
        
        if case == "Upper":
            password = make_uppercase(password, index)
        elif case == "Lower":
            password = make_lowercase(password, index)
    elif action == "Insert":
        cmd = command[0]
        index = int(command[1])
        char = command[2]
        
        password = insert_character(password, index, char)
    elif action == "Replace":
        cmd = command[0]
        char = command[1]
        value = int(command[2])
        
        password = replace_character(password, char, value)
    elif action == "Validation":
        is_valid_password(password)
        
