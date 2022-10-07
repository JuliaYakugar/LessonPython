import random

N = int(input('Введите N: '))

arr = []
i = 0
while i < N:
    arr.append(random.randint(-N, N))
    i += 1
print(arr)

str = input(f'Укажите индексы элементов для произведения от 0 до {N} через запятую: ').split(',')
mult = 1

for i in str:
    mult = mult * arr[int(i)]
print(mult)

j = 0
while j < N:
    index1 = random.randint(0, N-1)
    index2 = random.randint(0, N-1)
    arr[index1],arr[index2] = arr[index2],arr[index1]
    j += 1
print(arr)