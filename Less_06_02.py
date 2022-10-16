import random

arr = [i for i in range(1, random.randint(1, 10))]
arr = list(map(lambda j: int(random.randint(0, 100)), arr))

summa = sum(filter(lambda x: x%2 != 0, arr), 0)

print(arr)
print(summa)