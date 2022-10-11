n = int(input('Введите n: '))
mult = []
s = 2
while n > 1:
    if n % s == 0:
        mult.append(s)
        n = n/s
    else:
        s += 1
print(mult)