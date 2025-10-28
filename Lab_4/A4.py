def start_with(card):
    first = int(card[0])
    second = int(card[1])

    if first == 3 and (second == 4 or second == 7):
        return "American Express"
    elif first == 5 and second >= 1 and second <= 5:
        return "MasterCard"
    elif first == 4:
        return "Visa"
    else:
        return "Unknown"

def length(card):
    card_len = len(card)

    if card_len == 15 and start_with(card) == "American Express":
        return "American Express"
    elif card_len == 16 and start_with(card) == "MasterCard":
        return "MasterCard"
    elif (card_len == 13 or card_len == 16) and start_with(card) == "Visa":
        return "Visa"
    else:
        return "Unknown"


def lunar(card):
    total = 0
    reversed_card = card[::-1]

    for i in range(len(reversed_card)):
        digit = int(reversed_card[i])

        if i % 2 == 1:
            double_digit = digit * 2
            if double_digit < 10:
                total += double_digit
            else:
                total += double_digit // 10 + double_digit % 10
        else:
            total += digit

    return total % 10 == 0


card = input("Hомер банковской карты: ")

if lunar(card):
    a = start_with(card)
    b = length(card)

    if a == b and a != "Unknown":
        print(f"Валидная карта: {a}")
    else:
        print("Неизвестный тип карты или несоответствие")
else:
    print("Невалидный номер карты")