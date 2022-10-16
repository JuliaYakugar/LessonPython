x = input('Введите число: ').replace(',',' ').replace('.', ' ').replace('', ' ').split()
x = map(lambda i: int(i), x)
print(sum(x, 0))