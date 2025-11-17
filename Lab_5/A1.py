text = input("Enter a sentence: ")
position_1 = 0
position_2 = 0

while(position_1 != -1 and position_2 != -1):
    position_1 = text.rfind('(')
    position_2 = text.rfind(')')

    text = text.replace(text[position_1:position_2 + 1], '')

print(text)

