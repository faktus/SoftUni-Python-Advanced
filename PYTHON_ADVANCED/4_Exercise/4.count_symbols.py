text = tuple(list(input()))
text_dictionery = {}

for i in range(len(text)):
    
    letter = text[i]

    if letter not in text_dictionery:
        text_dictionery[letter] = text.count(letter)

sorted_text = sorted(text_dictionery)


for i in sorted_text:
    print(f'{i}: {text_dictionery[i]} time/s')