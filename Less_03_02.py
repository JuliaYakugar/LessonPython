import random
import math

arr = []
i = 0
while i < random.randint(1, 10):
    arr.append(int(random.randint(0, 10)))
    i += 1
print(arr)

j = 1
arr_new = []
while j <= math.ceil((len(arr))/2):
    arr_new.append(arr[j-1]*arr[-j])
    j += 1
print(arr_new) 