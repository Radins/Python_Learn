def cont_words(text):
    return len(text.split())

def count_chars(text):
    return len(text)

filename = input("Enter the filename: ")

with open(filename) as file:
    text = file.read()

print("There are " + str(cont_words(text)) + " words, and " + str(count_chars(text)) + " character in this text.")