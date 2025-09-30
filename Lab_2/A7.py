x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 >=1 and x1 <=8 or x2 >=1 and x2 <=8 or y1 >=1 and y1 <=8 or y2 >=1 and y2 <=8:
    if (x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0:
        print('YES')
        print('WHITE')
    elif (x1 + y1) % 2 == 1 and (x2 + y2) % 2 == 1:
        print('YES')
        print('BLACK')
    else:
        print('NO')