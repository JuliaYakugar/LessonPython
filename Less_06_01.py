arr = [1.1, 1.2, 3.1, 5, 10.01]
print(arr)

arr = list(map(lambda i: round(i - int(i), 2), arr))

print(arr)
print(max(arr)-min(arr))