s = 11
for i in range(1, s, 2):
    i = ' ' * ((s - i) // 2) + '*' * i
    print(i)
for i in range(s, 0, -2):
    i = ' ' * ((s - i) // 2) + '*' * i
    print(i)