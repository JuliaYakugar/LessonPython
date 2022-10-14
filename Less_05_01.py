stroka = 'авпкпуп вапвапабвапк ыуаыавы абвабвпрон'
podstroka = 'абв'

new_stroka = ' '.join(filter(lambda x: podstroka not in x, stroka.split()))

print(new_stroka)