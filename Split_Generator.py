text = input("Enter a text: ")

def split_word(word):
    yield word.split()

print(list(split_word(text)))