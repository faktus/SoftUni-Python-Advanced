text = input()
parentheses = []

for i in range(len(text)):
    if text[i] == '(':
        parentheses.append(i)
    elif text[i] == ')':
        print(text[parentheses.pop():i + 1])
