def store_words(notebook, input_str):
    words_and_definitions = input_str.split(" | ")
    for item in words_and_definitions:
        word, definition = item.split(": ")
        if word in notebook:
            notebook[word].append(definition)
        else:
            notebook[word] = [definition]

def test_words(notebook, input_str):
    words_to_test = input_str.split(" | ")
    for word in words_to_test:
        if word in notebook:
            print(f"{word}:")
            for definition in notebook[word]:
                print(f" -{definition}")

def hand_over(notebook):
    words_in_notebook = " ".join(notebook.keys())
    print(words_in_notebook)

notebook = {}
words_and_definitions_input = input()
store_words(notebook, words_and_definitions_input)

words_to_test_input = input()
test_command = input()

if test_command == "Test":
    test_words(notebook, words_to_test_input)
elif test_command == "Hand Over":
    hand_over(notebook)
else:
    print("Invalid command.")
