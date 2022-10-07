fib = int(input('Введите число: '))

fib1 = fib2 = 1
arr = []
arr.append(fib1)
arr.append(fib2)
 
for i in range(2, fib):
    fib1, fib2 = fib2, fib1 + fib2
    arr.append(fib2)

j = 0
arr_2 = []
while j < len(arr):
    if j%2 != 0:
        arr_2.append(arr[j] * -1)
    else:
        arr_2.append(arr[j])
    j += 1

arr_2.reverse()
arr_2.append(0)

list = arr_2 + arr
print(list)