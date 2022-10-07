N = int(input('Введите N: '))

arr = []
arr.append(1)
i = 2
while i <= N:
    arr.append(i * int(arr[i-2]))
    i += 1
print(arr)