with open('ChaseData.txt', 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines if line.strip()]

first_line = lines[0].split()
x_max = int(first_line[0])
y_max = int(first_line[1])

counter_cat = 0
x_cat = 0
y_cat = 0
distantion_cat = 0

counter_mouse = 0
x_mouse = 0
y_mouse = 0
distantion_mouse = 0

distance = 0

print("Cat and Mouse")
print("{:<12} {:<12} {:>8}".format("Cat", "Mouse", "Distance"))
print("-" * 35)

line_index = 1
while line_index < len(lines):
    line = lines[line_index]
    line_index += 1

    parts = line.split()
    operator = parts[0]

    if operator == "C":
        if counter_cat == 0:
            x_cat = int(parts[1])
            y_cat = int(parts[2])
            counter_cat = 1
        else:
            x_move_cat = int(parts[1])
            y_move_cat = int(parts[2])

            x_cat += x_move_cat
            y_cat += y_move_cat

            x_cat = x_cat % x_max
            y_cat = y_cat % y_max

            if x_cat < 1:
                x_cat += x_max
            if y_cat < 1:
                y_cat += y_max

            distantion_cat += abs(x_move_cat) + abs(y_move_cat)

    elif operator == "M":
        if counter_mouse == 0:
            x_mouse = int(parts[1])
            y_mouse = int(parts[2])
            counter_mouse = 1
        else:
            x_move_mouse = int(parts[1])
            y_move_mouse = int(parts[2])

            x_mouse += x_move_mouse
            y_mouse += y_move_mouse

            x_mouse = x_mouse % x_max
            y_mouse = y_mouse % y_max

            if x_mouse < 1:
                x_mouse += x_max
            if y_mouse < 1:
                y_mouse += y_max

            distantion_mouse += abs(x_move_mouse) + abs(y_move_mouse)

    elif operator == "P":
        if counter_cat > 0:
            cat_str = "({:2},{:2})".format(x_cat, y_cat)
        else:
            cat_str = "(??,??)"

        if counter_mouse > 0:
            mouse_str = "({:2},{:2})".format(x_mouse, y_mouse)
        else:
            mouse_str = "(??,??)"

        if counter_cat > 0 and counter_mouse > 0:
            distance = abs(x_cat - x_mouse) + abs(y_cat - y_mouse)
            distance_str = "{:2}".format(distance)
        else:
            distance_str = ""

        print("{:<12} {:<12} {:>8}".format(cat_str, mouse_str, distance_str))

    if counter_cat > 0 and counter_mouse > 0:
        distance = abs(x_cat - x_mouse) + abs(y_cat - y_mouse)
        if distance == 0:
            print("-" * 35)
            print("{:15} {:<15} {}".format("Distance", "Mouse", "Cat"))
            print("{:15} {:<15} {}".format("", distantion_mouse, distantion_cat))
            print("Cat caught mouse at: (" + str(x_cat) + ", " + str(y_cat) + ")")
            break

if counter_cat > 0 and counter_mouse > 0 and distance > 0:
    print("-" * 35)
    print("{:15} {:<15} {}".format("Distance", "Mouse", "Cat"))
    print("{:15} {:<15} {}".format("", distantion_mouse, distantion_cat))
    print("Mouse evaded Cat")