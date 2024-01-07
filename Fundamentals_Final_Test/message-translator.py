import re

def is_valid_string(s):
    # Check if the string matches the valid pattern
    pattern = r'^!([A-Z][a-z]+)!: \[([A-Za-z]+)\]$'
    match = re.match(pattern, s)
    if not match:
        return False

    command, text = match.groups()
    if len(command) < 3 or len(text) < 8:
        return False

    return True

def translate_string(s):
    command, text = re.match(r'^!([A-Z][a-z]+)!: \[([A-Za-z]+)\]$', s).groups()
    translated_text = " ".join(str(ord(char)) for char in text)
    return f"{command}:{translated_text}"

n = int(input("Enter the number of strings: "))
for _ in range(n):
    s = input("Enter the string: ")
    if is_valid_string(s):
        translated_string = translate_string(s)
        print("Valid string:", translated_string)
    else:
        print("The message is invalid")
