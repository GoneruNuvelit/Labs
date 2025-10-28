def rect(n, m, sym):
    print(f"Прямоугольник, размером {n}×{m}: ")
    for i in range(n):
        print(sym * m)

def triang(n, sym):
    print(f"Треугольник, высотой {n}: ")
    for i in range(n):
        print(sym * (i+1))

def border(n, m, sym):
    print(f"Рамка, размером {n}×{m}: ")
    for i in range(n):
        if i == 0 or i == n-1:
            print(sym * m)
        else:
            print(sym, end ="")
            print(" " * (m - 2), end ="")
            print(sym)

n = int(input("Высота фигуры: "))
m = int(input("Ширина фигуры: "))
sym = input("Печатаемый символ: ")

rect(n, m, sym)
print()
triang(n, sym)
print()
border(n, m, sym)