import xml.etree.ElementTree as et

def load_users_data():
    users_data = et.parse("users.xml")
    users_root = users_data.getroot()
    return users_root

def load_workouts_data():
    workouts_data = et.parse("workouts.xml")
    workouts_root = workouts_data.getroot()
    return workouts_root

def get_stats(users, workouts):
    training_count = len(workouts.findall(".//workout_id"))

    users_count = len(users.findall(".//user_id"))

    calories = workouts.findall(".//calories")
    all_calories = 0
    for cal in calories:
        all_calories += int(cal.text)

    time = workouts.findall(".//duration")
    all_time = 0
    for spend_time in time:
        all_time += int(spend_time.text) / 60
    total_time = round(all_time, 1)

    distance = workouts.findall(".//distance")
    all_distance = 0
    for dist in distance:
        all_distance += float(dist.text)
    total_distance = round(all_distance, 1)

    print("ОБЩАЯ СТАТИСТИКА\n"
          "============================\n"
          f"Всего тренировок: {training_count}\n"
          f"Всего пользователей: {users_count}\n"
          f"Сожжено калорий: {all_calories}\n"
          f"Общее время: {total_distance} часов\n"
          f"Пройдено дистанции: {total_time} км\n")

users = load_users_data()
work = load_workouts_data()
get_stats(users, work)