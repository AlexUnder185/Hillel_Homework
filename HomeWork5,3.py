import string

text = input("Enter your text: ")

for char in string.punctuation:
    text = text.replace(char, '')

text = text.title()

words = text.split()

hashtag = "#" + "".join(words)
print(hashtag[:140])




