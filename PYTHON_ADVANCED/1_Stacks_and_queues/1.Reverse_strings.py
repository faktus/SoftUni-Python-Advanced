text = input()
text = [letter for letter in text]

while text:
    print(text.pop(), end='')