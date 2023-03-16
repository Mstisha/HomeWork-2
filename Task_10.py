from random import randint
n = int(input("Введите количество монет: "))
min = 0
for i in range(n):
    c = randint(1, 2)
    if c == 2:
        min += 1    
print(f'Минимальное количество монет, которые нужно перевернуть: {min}')