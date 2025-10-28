pack = input("Пакет данных: ")

length = len(pack)

lost_pack = 0
curent_strike = 0
longest_lost_pack_strike = 0

for i in range(length):

    if pack[i] == '0':
        lost_pack += 1
        curent_strike += 1

        if curent_strike > longest_lost_pack_strike:
            longest_lost_pack_strike = curent_strike
    else:
        curent_strike = 0

lost_percentage = round(lost_pack * 100 / length, 1)

print(f"Общее количество пакетов: {length}")
print(f"Количество потерянных пакетов: {lost_pack}")
print(f"Длина самой длинной последовательности потерянных пакетов: {longest_lost_pack_strike}")
print(f"Процент потерь: {lost_percentage}%")
print("Качество связи:", end = " ")

if lost_percentage < 1:
    print("Отличное качество")
elif lost_percentage < 5:
    print("Хорошее качество")
elif lost_percentage < 10:
    print("Удовлетворительное качество")
elif lost_percentage < 20:
    print("Плохое качество")
else:
    print("Критическое состояние сети")