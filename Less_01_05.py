import math

ax = int(input('Введите Ax: '))
ay = int(input('Введите Ay: '))
bx = int(input('Введите Bx: '))
by = int(input('Введите By: '))
print(int(math.sqrt(math.pow((ax - bx), 2) + math.pow((ay - by), 2)) * 100) / 100)