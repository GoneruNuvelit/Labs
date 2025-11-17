s = input("Write a words: ").split()

for word in s:
    if len(word) < 3:
        continue
    print(word[0].upper(), end="")