from random import randint
num1 = randint(1, 1000)
num2 = randint(1, 1000)
s = num1 + num2
p = num1 * num2
print(s, p)
for i in range(10001):
    if (i * i) - (s * i) + p == 0:
        print(i)