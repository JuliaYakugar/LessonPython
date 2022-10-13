from dataclasses import replace
import random

k = int(input('Введите степень k: '))

def func(name, k):
    stroka = ''
    while k >= 0:
        stroka = stroka + str(random.randint(0, 100))
        if k == 0:
            stroka = stroka + ' = 0'
            break
        stroka = stroka + 'x**'
        stroka  = stroka + str(k) + ' + '
        k -= 1
    print(stroka)

    with open(name,'w') as data:
        data.write(stroka)

func('less_04_05_01.txt', k)
func('less_04_05_02.txt', k)

def read_file(name):
    data = open(name, 'r')
    for line in data:
        mas_number = line.replace(' + ', ' ').replace('x**', ' ').replace(' = ', ' ').split()
    data.close()
    c = 0
    carrent_mas = []
    while c < len(mas_number):
        if c%2 == 0:
            carrent_mas.append(mas_number[c])
        c += 1
    return(carrent_mas)

kaf1 = read_file('less_04_05_01.txt')
kaf2 = read_file('less_04_05_02.txt')

i = 0
carrent_str = ''
while i < len(kaf1):
    carrent_str = carrent_str + str(int(kaf1[i]) + int(kaf2[i]))
    if i == len(kaf1) - 1:
        carrent_str = carrent_str + ' = 0'
        break
    carrent_str = carrent_str + 'x**'
    carrent_str = carrent_str + str(len(kaf1) - i - 1)
    carrent_str = carrent_str + ' + '
    i += 1

print(carrent_str)

with open('less_04_05_03.txt','w') as data:
    data.write(carrent_str)