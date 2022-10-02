x = int(input('Введите x: '))
y = int(input('Введите y: '))
z = int(input('Введите z: '))

if (not (x or y or z)) == ((not x) and (not y) and (not z)):
    print('Условие верно')
else:
    print('Условие неверно')