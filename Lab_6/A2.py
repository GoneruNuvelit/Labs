import xml.etree.ElementTree as et

def load_users_data():
    users_data = et.parse("users.xml")
    users_root = users_data.getroot()
    return users_root

def load_workouts_data():
    workouts_data = et.parse("workouts.xml")
    workouts_root = workouts_data.getroot()
    return workouts_root

def analyze_user_activity(users):
    workouts_data = et.parse("workouts.xml")
    workouts = workouts_data.getroot()

    user_data_training = {}

    for user_el in users.findall(".//user"):
        user_id = user_el.find("user_id").text
        name = user_el.find("name").text
        fitness_level = user_el.find("fitness_level").text

        user_data_training[user_id] = {
            'name': name,
            'fitness_level': fitness_level,
            'training_counts': 0,
            'calories': 0,
            'time_minutes': 0
        }

    for work_el in workouts.findall(".//workout"):
        user_id = work_el.find("user_id").text

        if user_id in user_data_training:
            user_data_training[user_id]['training_counts'] += 1
            user_data_training[user_id]['calories'] += int(work_el.find("calories").text)
            user_data_training[user_id]['time_minutes'] += int(work_el.find("duration").text)

    users_list = []
    for user_id, data in user_data_training.items():
        user_info = data.copy()
        user_info['id'] = user_id
        user_info['hours'] = round((user_info['time_minutes'] / 60), 1)
        users_list.append(user_info)

    users_length = len(users_list)

    print("ТОП-3 САМЫХ АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")
    print("======================================")

    top_users = []
    used_indices = set()
    for top in range(3):
        max_value = -1
        max_index = -1

        for j in range(users_length):
            if j not in used_indices:
                if users_list[j]['training_counts'] > max_value:
                    max_value = users_list[j]['training_counts']
                    max_index = j

        if max_index != -1:
            used_indices.add(max_index)
            top_users.append(users_list[max_index])

            user = users_list[max_index]
            print(f"{top + 1}. {user['name']} ({user['fitness_level']})\n"
                  f"Тренировок: {user['training_counts']}\n"
                  f"Калорий: {user['calories']}\n"
                  f"Время: {user['hours']} часов\n")


def analyze_workout_types(workouts_root):
    types_data = {}

    for workout in workouts_root.findall(".//workout"):
        work_type = workout.find("type").text
        duration = int(workout.find("duration").text)
        calories = int(workout.find("calories").text)

        if work_type not in types_data:
            types_data[work_type] = {
                'count': 0,
                'total_time': 0,
                'total_calories': 0
            }

        types_data[work_type]['count'] += 1
        types_data[work_type]['total_time'] += duration
        types_data[work_type]['total_calories'] += calories

    total_traininigs = sum(data['count'] for data in types_data.values())

    print("РАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")
    for work_type, data in types_data.items():
        percentage = (data['count'] / total_traininigs) * 100
        avg_duration = data['total_time'] / data['count']
        avg_calories = data['total_calories'] / data['count']

        print(f"{work_type.capitalize()}: {data['count']} тренировок ({percentage:.1f}%)\n\t"
              f"Средняя длительность: {round(avg_duration)} мин\n\t"
              f"Средние калории: {round(avg_calories)} ккал")


def find_user_workouts(users_root, user_name):
    user_id = None
    for user in users_root.findall(".//user"):
        if user.find("name").text.lower() == user_name.lower():
            user_id = user.find("user_id").text
            break

    if not user_id:
        return []

    workouts_tree = et.parse("workouts.xml")
    workouts_root = workouts_tree.getroot()

    user_workouts = []
    for workout in workouts_root.findall(".//workout"):
        if workout.find("user_id").text == user_id:
            workout_data = {
                'workout_id': workout.find("workout_id").text,
                'date': workout.find("date").text,
                'type': workout.find("type").text,
                'time': int(workout.find("duration").text),
                'distance': float(workout.find("distance").text),
                'calories': int(workout.find("calories").text),
                'avg_heart_bit': int(workout.find("avg_heart_rate").text),
                'intensity': workout.find("intensity").text
            }
            user_workouts.append(workout_data)

    return user_workouts

def analyze_user(user_name, workouts_root):
    users = et.parse("users.xml")
    users_data = users.getroot()

    user_data = None
    for user in users_data.findall(".//user"):
        if user.find("name").text.lower() == user_name.lower():
            user_data = {
                'name': user.find("name").text,
                'age': int(user.find("age").text),
                'weight': int(user.find("weight").text),
                'fitness_level': user.find("fitness_level").text
            }
            break

    if not user_data:
        print("Пользователь не найден")
        return

    user_id = None
    for user in users_data.findall(".//user"):
        if user.find("name").text.lower() == user_name.lower():
            user_id = user.find("user_id").text
            break

    user_workouts = []
    for workout in workouts_root.findall(".//workout"):
        if workout.find("user_id").text == user_id:
            workout_info = {
                'type': workout.find("type").text,
                'duration': int(workout.find("duration").text),
                'distance': float(workout.find("distance").text),
                'calories': int(workout.find("calories").text)
            }
            user_workouts.append(workout_info)

    total_workouts = len(user_workouts)

    total_calories = 0
    for work in user_workouts:
        total_calories += work['calories']

    total_duration = 0
    for work in user_workouts:
        total_duration += work['duration']
    total_duration = round((total_duration / 60), 1)

    total_distance = 0
    for work in user_workouts:
        total_distance += work['distance']
    total_distance = round(total_distance, 1)

    if total_workouts > 0:
        avg_calories = round(total_calories / total_workouts)
    else:
        avg_calories = 0

    print(f"ДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: {user_data['name']}\n"
          "===========================================\n"
          f"Возраст: {user_data['age']} лет, Вес: {user_data['weight']} кг\n"
          f"Уровень: {user_data['fitness_level']}\n"
          f"Тренировок: {total_workouts}\n"
          f"Сожжено калорий: {total_calories}\n"
          f"Общее время: {total_duration} часов\n"
          f"Пройдено дистанции: {total_distance} км\n"
          f"Средние калории за тренировку: {avg_calories}")

    type_count = {}
    for work in user_workouts:
        type_work = work['type']
        if type_work not in type_count:
            type_count[type_work] = 1
        else:
            type_count[type_work] += 1

    if len(type_count) > 0:
        max_count = 0
        favorite_type = ""
        for type_key, count in type_count.items():
            if count > max_count:
                max_count = count
                favorite_type = type_key
        print(f"Любимый тип тренировки: {favorite_type}")

analyze_user_activity(load_users_data())
analyze_workout_types(load_workouts_data())
print(find_user_workouts(load_users_data(), "Анна"))
analyze_user("Борис", load_workouts_data())