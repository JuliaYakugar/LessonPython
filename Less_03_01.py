import random

arr = []
i = 0
summa = 0
while i < random.randint(1, 10):
    arr.append(int(random.randint(0, 100)))
    if i%2 != 0:
        summa += arr[i]
    i += 1
print(arr)
print(summa)