# 1. Вычислить число c заданной точностью d
Num = float(input('Введите число: '))
d = input('Введите точность: ')
d = d.split('.')
if len(d) == 1:
    print(int(Num))
else:
    print(round(Num, len(d[1])))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = int(input('Введите натуральное число: '))
list = []
for i in range (2, N+1):
    if N % i == 0:
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        else:
            list.append(i)
print(list)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности
list = list(map(int, input("Задайте через пробел последовательность чисел: ").split()))
res = []
for i in list:
    if list.count(i) == 1:
        res.append(i)
print(res)

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
import random

def get_polynomial(koeff):
    poly = '+'.join([f'{(j, "")[j == 1]}*x^{i}' for i, j in enumerate(koeff) if j][::-1])
    poly = poly.replace('x^1+', 'x+')
    poly = poly.replace('*x^0', '')
    poly += '=0'
    return poly

k = int(input('Введите натуральную степень k: '))
mas_cof = []
for i in range(k + 1):
    mas_cof.append(random.randint(0, 100))
polynom = get_polynomial(mas_cof)
print(polynom)

with open('Polynomial.txt', 'w') as data:
    data.write(polynom)

# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import re
import itertools

# получение данных из файла
def read_file(file):
    with open(str(file), 'r') as data:
        return data.read()

# Получение списка кортежей каждого (<коэффициент>, <степень>)
def convert_pol(pol):
    pol = pol.replace('=0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol

# Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)
def fold_pols(pol1, pol2):
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res

# Составление итогового многочлена
def get_sum_pol(pol):
    var = ['*x^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1':
            del x[-1]
            x[-1] = '*x'
        x.append('+')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = '=0'
    return "".join(map(str, new_pol))

file1 = 'Polynomial_1.txt'
file2 = 'Polynomial_2.txt'
pol1 = read_file(file1)
pol2 = read_file(file2)
pol_1 = convert_pol(pol1)
pol_2 = convert_pol(pol2)
pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
with open('Polynomial_sum.txt', 'w') as data:
    data.write(pol_sum)






