import random
import time

N = int(input("Введите количество примеров:"))

total_time = 0
rights_answers = 0

for i in range(1, N + 1):
    print(f"Вопрос {i}/{N}")

    a = random.randint(2, 9)
    b = random.randint(2, 9)
    c = a * b

    while True:
        try:
            start_time = time.time()
            c_user = int(input(f"{a} × {b} = "))
            end_time = time.time()
            break
        except ValueError:
            print("Ошибка! Введите целое число.")

    time_spent = end_time - start_time
    total_time += time_spent

    if c_user == c:
        print(f"Верно! (Время: {time_spent} сек)")
        rights_answers += 1
    else:
        print(f"Неверно! (Время: {time_spent} сек)")

average_time = total_time / N
persent_answers = rights_answers * 100 / N

print("==================================================")
print("СТАТИСТИКА:")
print("==================================================")
print(f"Общее время: {total_time:.1f} сек")
print(f"Среднее время на вопрос: {average_time:.1f} сек")
print(f"Правильных ответов: {rights_answers}/{N}")
print(f"Процент правильных: {persent_answers:.1f}%")