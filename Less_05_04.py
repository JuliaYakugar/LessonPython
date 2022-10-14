stroka = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'
encoding = ''
char = ''
count = 1

for s in stroka:
    if s != char:
        if char: 
            encoding += str(count) + char
        count = 1
        char = s
    else:
        count += 1
else:
    encoding += str(count) + char
    print(encoding)