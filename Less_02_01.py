summa = 0
x = input('Введите число: ').replace(',',' ').replace('.', ' ').replace('', ' ').split()
for i in x:
    summa += int(i)
print(summa)