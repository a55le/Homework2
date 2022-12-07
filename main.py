#Задание 1
a = float(input("Введите число"))
b = str(a)
c = list(b)
d = 0
for i in range (len(c)):
    if b[i] != '.':
        d = d + int(b[i])
print(d)
#Задание 2
n = int(input("Введитте n"))
a = 6
for i in range(n):
    a = (1 + 1/n)**n
    n += 1
    print(a)
    a = a + n
print(a)
#Задание 3
import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(list)):
    random_choice = random.choice(list)
    new_list[i] = random_choice
    list.remove(random_choice)
print(new_list)
#Задание 4(дополнительное):
#Этап 1
import random
a = [random.randint(1000,9999), random.randint(1000,9999), random.randint(1000,9999), random.randint(1000,9999), random.randint(1000,9999), random.randint(1000,9999), random.randint(1000,9999), random.randint(1000,9999), random.randint(1000,9999), random.randint(1000,9999), ]
print(a)
#Этап 2
b = ['','','','','','','','','', '']
number = input("Введите число для удаления из элементов массива")
for i in range(len(a)):
    replace_a = str(a[i])
    b[i] = replace_a.replace(number, "")
print(b)
#Этап 3
c = ['','','','','','','','','','']
for i in range(len(b)):
    list_b = list(b[i])
    c1 = 0
    for i2 in range(len(list_b)):
        c1 = c1 + int(list_b[i2])
    list_c = list(str(c1))
    if len(str(c1)) != 1:
        c[i] = int(list_c[0])+int(list_c[1])
    else:
        c[i] = c1
print(c)
#Этап 4
d = ['','','','','','','','','','']
return_simvols = ['']
for i in range(len(c)):
    if c[i] in d:
        continue
    else:
        d[i] = c[i]
d = list(filter(None, d))
print(d)