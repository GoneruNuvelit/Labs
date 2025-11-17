import re

text = input("Enter a sentence: ")

text = re.split(r'(?<=[.?!]) ', text)

length = len(text)

i = 0

for i in range(length):
    print(text[i].strip())

print("Sentences in text: ", i+1)