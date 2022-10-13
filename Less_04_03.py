import random

arr = []
i = 0
while i < 10:
    arr.append(random.randint(0, 10))
    i += 1
print(arr)

arr_new = []
for j in arr:
    count = 0
    for k in arr:
        if j == k:
            count += 1
            if count > 1:
                break
    if count == 1:
        arr_new.append(j)
print(arr_new)