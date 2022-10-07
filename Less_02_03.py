n = int(input('Введите n: '))

arr = []
i = 1
while i <= n:
    arr.append(round((1 + 1/i)**i))
    i += 1
print(sum(arr))