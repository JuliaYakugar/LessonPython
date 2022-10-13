import random

k = int(input('Введите степень k: '))
l = k

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

with open('less_04_04.txt','w') as data:
	data.write('Mnogochlen stepeni ' + str(l) + ' => ' + stroka)