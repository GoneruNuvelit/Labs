n = int(input())

h = n // 3600
m = (n - h * 3600) // 60
s = n % 60

print('{}:{:02}:{:02}'.format(h, m, s))