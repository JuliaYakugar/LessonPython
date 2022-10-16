n = int(input('Введите n: '))

arr = [i for i in range(1, n+1)]
arr = list(map(lambda j: round((1 + 1/j)**j), arr))

print(sum(arr))