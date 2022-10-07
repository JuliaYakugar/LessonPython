arr = [1.1, 1.2, 3.1, 5, 10.01]
print(arr)

i = 0
while i < len(arr):
    arr[i] = round(arr[i] - int(arr[i]), 2)
    i += 1

print(max(arr)-min(arr))